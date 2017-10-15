from rest_framework.authentication import (
    BaseAuthentication
)

from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from django.core.exceptions import ObjectDoesNotExist
from task.models import UserSession



class MutipleTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION", "")
        print "token",token
        if not token:
            msg = ('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        try:
            token = token.decode()
        except UnicodeError:
            msg = (
                'Invalid token header.'
                ' Token string should not contain invalid characters.'
            )
            raise exceptions.AuthenticationFailed(msg)
        try:
            user_session = UserSession.objects.select_related(
                'user').get(token=token)
        except ObjectDoesNotExist:
            msg = ('Invalid token header. Token doesn\'t exist')
            raise exceptions.AuthenticationFailed(msg)
        return (user_session, None)
