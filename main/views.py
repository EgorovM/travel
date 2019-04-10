# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts 			import render, HttpResponseRedirect, redirect, HttpResponse
from .models					import Consumer, Entrepreneur, Administrator, Location, Point, Filter
from django.db 					import IntegrityError
from django.core.paginator 		import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth 		import authenticate
from django.contrib.auth 		import logout
from django.contrib 			import auth
from PIL      					import Image
from pytz 						import timezone
from datetime 					import datetime, timedelta
from django.http 				import JsonResponse
import pandas as pd
import sqlite3
import json
import pytz
import os
import qrcode

def get_correct_profile(user):
	status = user.email

	if "administrator" in status:
		profile = Administrator.objects.get(user = user)
	elif "consumer" in status:
		profile = Consumer.objects.get(user = user)
	else:
		profile = Entrepreneur.objects.get(user = user)

	return profile

def correct_filter(profile):
	entrepreneurs = []

	for entrepreneur in Entrepreneur.objects.all():
		if entrepreneur.location == profile.user.filter.location:
			if entrepreneur.price <= profile.user.filter.price:
				if profile.user.filter.home == True and entrepreneur.status == "home":
					entrepreneurs.append(entrepreneur)
				if profile.user.filter.repair == True and entrepreneur.status == "repair":
					entrepreneurs.append(entrepreneur)

	return entrepreneurs

def index(request):

	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login")
	context = {}
	profile = get_correct_profile(request.user)

	if len(correct_filter(profile)) != 0:
		context["entrepreneurs"] = correct_filter(profile)
		context["amount"] = len(context["entrepreneurs"])
	context["locations"]     = Location.objects.all()
	context["profile"] = profile

	request = render(request, 'main/index.html', context)

	return request

def filter(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login")
	context = {}

	profile = get_correct_profile(request.user)

	if request.method == "POST":
		if "search" in request.POST:
			profile.user.filter.price    = request.POST["price"]
			profile.user.filter.location = Location.objects.get(location = request.POST["location"])

			if request.POST.get("home") == "on":
				profile.user.filter.home = True
			else:
				profile.user.filter.home = False
			
			if request.POST.get("repair") == "on":
				profile.user.filter.repair = True
			else:
				profile.user.filter.repair = False
			
			profile.user.filter.save()

			return HttpResponseRedirect("/")

	context["profile"] = profile
	context["locations"] = Location.objects.all()

	request = render(request, 'main/filter.html', context)
	return request

def login(request):
	context = {}

	if request.method == "POST":
		if "login_btn" in request.POST:
			username = request.POST["username"]
			password = request.POST["password"]

			if login != "" and password != "":
				user = authenticate(username = username, password = password)

				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect("/")
				else:
					context["message"] = "Такого пользователя не существует"
			else:
				context["message"] = "Заполните все поля, пожалуйста"
		


	request = render(request, 'main/login.html', context)

	return request

def register(request):
	context = {}

	if request.method == "POST":
		if "ok_button" in request.POST:
			username     = request.POST["username"]
			password     = request.POST["password"]
			status 		 = request.POST["status"]

			if username !='' and password !='':
				try:
					user = User.objects.create_user(username = username, password = password)
					user.save()

				except IntegrityError:
					context["message"] = "Такой аккаунт уже существует"
					response = render(request, 'main/register.html', context)
					return response

				if status == "consumer":
					user.email = status + "@m.ru"
					profile = Consumer(user = user)
				elif status == "home" or status == "repair":
					user.email = status + "@m.ru"
					profile = Entrepreneur(user = user)
					location = Location.objects.get(location = request.POST["location"])
					profile.location = location
					profile.status = status
				else:
					user.email = "administrator@m.ru"
					profile = Administrator(user = user)
					location = Location(location = request.POST["location"])
					location.save()
					profile.location = location

				Filter.objects.create(user = user)
				profile.user.save()
				profile.save()

				user = authenticate(username = username, password = password)

				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect("/settings")
			else:
				context['message'] = 'Заполните все поля, пожалуйста'

	context["locations"] = Location.objects.all()
	request = render(request, 'main/register.html', context)

	return request


def settings(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login")
	context = {}

	profile = get_correct_profile(request.user)

	status = request.user.email
	if request.method == "POST":
		if "save" in request.POST:
			profile.user.first_name = request.POST["first_name"]
			profile.user.last_name  = request.POST["last_name"]
			profile.telephone  = request.POST["telephone"]
			profile.about      = request.POST["about"]

			if "home" in status or "repair" in status:
				profile.address  = request.POST["address"]
				profile.price    = request.POST["price"]
				profile.addition = request.POST["addition"]
			elif "consumer" in status:
				profile.age    = request.POST["age"]
				profile.wishes = request.POST["wishes"]
			else:
				profile.address = request.POST["address"]
			profile.save()
			profile.user.save()

			context["message"] = "Данные изменены!"

	context["profile"] = profile 

	request = render(request, 'main/settings.html', context)

	return request

def profile(request, user_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login")

	context = {}
	view_user = User.objects.get(id = user_id)
	view_profile = get_correct_profile(view_user)

	context["view_profile"] = view_profile
	context["profile"] = get_correct_profile(user = request.user)

	request = render(request, 'main/profile.html', context)
	return request

def confirm(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login")

	context = {}
	context["profile"] = get_correct_profile(request.user)

	request = render(request, 'main/confirm.html', context)

	return request
	
def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/login')

