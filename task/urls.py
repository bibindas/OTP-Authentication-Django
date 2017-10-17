from django.conf.urls import url
from . import views

urlpatterns = [
				url(r'^$',views.login,name='login'),
				url(r'^signup/$',views.signup,name='signup'),
				url(r'^home/$',views.home,name='home'),
				url(r'^details/$',views.details,name='details'),

				
			]