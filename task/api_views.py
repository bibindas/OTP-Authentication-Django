import string
import random
import uuid
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from task.auth import MutipleTokenAuthentication

from task.models import (
    AppUser,
    City,
    Country,
    Countrylanguage,
    UserSession,
)

def otp_generator(user,size=6, chars=string.digits):
    current_otps = UserSession.objects.filter(user=user).values_list('otp',flat=True)
    otp = ''.join(random.choice(chars) for _ in range(size))
    while otp in current_otps:
        otp = ''.join(random.choice(chars) for _ in range(size))
    return otp


class Signup(APIView):
    # API for registering user
    def post(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        gender = request.data.get("gender")
        if not first_name or not last_name or not email or not gender or not phone_number:
            return Response(
                {'status':"Failed"},
                status=status.HTTP_400_BAD_REQUEST)
        user= AppUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    gender=gender,
                    phone_number=phone_number)
        return Response(
                {'status':"success"},
                status=status.HTTP_201_CREATED)             


class Login(APIView):
    # API for login
    def post(self,request):
        type_ = request.data.get("type_")
        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        if type_ == 'email':
            if not email:
                return Response(
                    {'status':"email field requeired"},
                    status=status.HTTP_400_BAD_REQUEST)        
            else:
                user = AppUser.objects.get(email=email)
        if type_ == 'phonenumber':
            if not phone_number:
                return Response(
                    {'status':"phonenumber field requeired"},
                    status=status.HTTP_400_BAD_REQUEST)        
            else:
                user = AppUser.objects.get(phone_number=phone_number)
        otp = otp_generator(user=user)
        user_token = UserSession.objects.create(user=user,token=str(uuid.uuid4()),otp=otp)

        # sent otp here
        if type_ == 'email':
            email = EmailMessage("OTP",otp, to=[email])
            email.send()
        return Response(
            {'status':'success'},
            status=status.HTTP_201_CREATED)


class Logout(APIView):
    authentication_classes = (MutipleTokenAuthentication,)

    def post(self,request):
        user_session = UserSession.objects.get(token=request.user.token)
        user_session.delete()
        return Response(
            {'status':'OK'},
            status=status.HTTP_200_OK)            