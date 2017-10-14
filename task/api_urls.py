from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from task import api_views

urlpatterns = format_suffix_patterns([
	url(r'^signup/$',api_views.Signup.as_view(),name='signup'),
	url(r'^login/$',api_views.Login.as_view(),name='login')
])