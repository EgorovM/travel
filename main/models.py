from __future__                     import unicode_literals
from django.utils.encoding          import python_2_unicode_compatible
from django.db                      import models
from django.contrib.auth.models     import User
from datetime 					    import datetime
from django 						import forms
from django.utils import timezone

RATE = (
	("Beginner", "Новичок"),
	("Expirienser", "Опытный"),
	("Old", "Бывалый"),
)
STATUS = (
	("repair", "Ремонт"),
	("home", "Жилье")
)

class Point(models.Model):
	consumer     = models.ForeignKey('Consumer')
	entrepreneur = models.ForeignKey('Entrepreneur')
	point        = models.IntegerField(default = 0)
	date         = models.DateField(default = timezone.now())

	def __str__(self):
		return str(consumer) + ' ' + str(entrepreneur)

class Consumer(models.Model):
	user      = models.OneToOneField(User)
	rate      = models.CharField(max_length = 50,default = "Beginner", choices = RATE)
	telephone = models.CharField(max_length = 100,default = "Ни скажу!")
	age       = models.IntegerField(default = 18)
	wishes    = models.CharField(max_length = 100, default = "Все не почём!")

	photo     = models.ImageField(upload_to = "images/", default = "images/user_default.jpg")

	def __str__(self):
		return str(self.user)

class Entrepreneur(models.Model):
	user      = models.OneToOneField(User)
	status    = models.CharField(max_length = 50, choices = STATUS)
	checked   = models.BooleanField(default = False)
	location  = models.OneToOneField('Location')
	address   = models.CharField(max_length = 100)
	price     = models.IntegerField(max_length = 100)

	telephone = models.CharField(max_length = 10)
	addition  = models.CharField(max_length = 500)

	photo     = models.ImageField(upload_to = "images/", default = "images/home_default.jpg")

	def __str__(self):
		return str(self.user)

class Administrator(models.Model):
	user     = models.OneToOneField(User)
	location = models.OneToOneField('Location')

	def __str__(self):
		return str(self.user)

class Location(models.Model):
	location = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.location)
