import string
import random
import uuid
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from task.auth import MutipleTokenAuthentication
from task.serializers import (
    CountrySerializer,
    CitySerializer,
    LanguageSerializer,
)
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
                {'status':"Failed",
                'message':"Bad parameters"},
                status=status.HTTP_200_OK)
        if AppUser.objects.filter(email=email).exists():
            return Response(
                {'status':"Failed",
                "messages": "Already registered"},
                status=status.HTTP_200_OK)  
        user= AppUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    gender=gender,
                    phone_number=phone_number)           
        return Response(
                {'status':"success",
                "messages":"Registered"},
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
            {'status':'success',
            'messages':'OTP sent'},
            status=status.HTTP_201_CREATED)


class Logout(APIView):
    authentication_classes = (MutipleTokenAuthentication,)

    def post(self,request):
        print request.user
        user_session = UserSession.objects.get(token=request.user.token)
        user_session.delete()
        return Response(
            {'status':'OK',
            'message':'success'},
            status=status.HTTP_200_OK)            


class OtpVerification(APIView):
    def post(self,request):
        type_ = request.data.get("type_")
        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        otp = request.data.get("otp")
        print "otp", otp
        print type_
        if not otp:
            return Response({
                'status':"failed",
                'message':"OTP required"
                },status=status.HTTP_400_BAD_REQUEST)  
        if type_ == 'email':
            try:
                user_session = UserSession.objects.get(user__email=email,otp=otp)
                print user_session
                return Response({'status':'OK',
                    'message':'success',
                    'token':user_session.token
                    },status=status.HTTP_200_OK)
            except:
                return Response({
                    'status':'failed',
                    'message':'Invalid OTP'
                    },status=status.HTTP_400_BAD_REQUEST)
        if type_ == 'phonenumber':
            try:
                user_session = UserSession.objects.get(user__phone_number=phone_number,otp=otp)
                return Response({'status':'OK',
                    'message':'success'
                    },status=status.HTTP_200_OK)
            except:
                return Response({
                    'status':'failed',
                    'message':'Invalid OTP'
                    },status=status.HTTP_400_BAD_REQUEST)    

class Search(APIView):
    authentication_classes = (MutipleTokenAuthentication,)

    def post(self,request):
        type_ = request.data.get("type_")
        search = request.data.get("search")
        search_list = []
        if type_ == "country":
            countrys = Country.objects.filter(name__istartswith=search)
            for country in countrys:
                search_list.append({'text':country.name,'value':country.name})

        if type_ == "city":
            citys = City.objects.filter(name__istartswith=search)
            for city in citys:
                search_list.append({'text':city.name,'value':city.name})
        if type_ == "countrylanguage":
            languages = Countrylanguage.objects.filter(language__istartswith=search)
            for language in languages:
                search_list.append({'text':language.language,'value':language.language})

        return Response({
            'status':'OK',
            'search_list':search_list,},status=status.HTTP_200_OK)


class Details(APIView):
    authentication_classes = (MutipleTokenAuthentication,)
    def post(self,request):
        type_ = request.data.get("type_")
        search = request.data.get("search")
        if type_ == "country":
            country = Country.objects.filter(name=search)

            data = CountrySerializer(country,many=True).data
            
        if type_ == "city":
            city = City.objects.filter(name=search)
            data = CitySerializer(city,many=True).data

        if type_ == "countrylanguage":
            countrylanguage = Countrylanguage.objects.filter(language=search)
            
            data = LanguageSerializer(countrylanguage,many=True).data
            

        return Response({
            'status':'OK',
            'data':data,
            },status=status.HTTP_200_OK)


class CountryDetails(APIView):
    authentication_classes = (MutipleTokenAuthentication,)

    def post(self,request):
        country = request.data.get('country')
        country_data = Country.objects.get(name=country)
        country_details = CountrySerializer(country).data

        return Response({
            'status':'OK',
            'country_details':country_details
            },status=status.HTTP_200_OK)
