from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone    
from .models import City,Country,Countrylanguage,AppUser
from django.urls import reverse
from django.db import connection

def login(request):
	return render(request,'task/login.html')

def signup(request):
	return render(request,'task/signup.html')

def home(request):
	return render(request,'task/home.html')	

def details(request):
	return render(request,'task/srchdetails.html')	 	