# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts 			import render, HttpResponseRedirect, redirect, HttpResponse
from .models					import Consumer, Entrepreneur, Administrator, Location
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

def index(request):
	context = {}
	context["entrepreneurs"] = Entrepreneur.objects.all()

	request = render(request, 'main/index.html', context)

	return request