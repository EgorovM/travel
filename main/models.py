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
SEX = (
	(False, "Женщина"),
	(True, "Мужчина"),
)

class Admin_Request(object):
	administrator = models.ForeignKey('Administrator')

	def __str__(self):
		return self.administrator
		
class Entr_Request(models.Model):
	administrator = models.ForeignKey('Administrator')
	consumer = models.OneToOneField('Consumer')

	def __str__(self):
		return str(self.consumer) + " " +str(self.location)

class Point(models.Model):
	consumer     = models.ForeignKey('Consumer')
	entrepreneur = models.ForeignKey('Entrepreneur')
	point        = models.IntegerField(default = 0)
	date         = models.DateField(default = timezone.now())

	def __str__(self):
		return str(self.consumer) + ' ' + str(self.entrepreneur)

class Filter(models.Model):
	user = models.OneToOneField(User)

	price    = models.IntegerField(default = 0)
	repair   = models.BooleanField(default = False)
	home     = models.BooleanField(default = False)
	location = models.ForeignKey('Location', null = True, blank = True)

	def __str__(self):
		return str(self.user) + " filters"

class Consumer(models.Model):
	user      = models.OneToOneField(User)
	rate      = models.CharField(max_length = 50,default = "Beginner", choices = RATE)
	telephone = models.CharField(max_length = 100,default = "Ни скажу!", blank = True)
	age       = models.IntegerField(default = 18, blank = True)
	wishes    = models.CharField(max_length = 100, default = "Все не почём!", blank = True)

	photo     = models.ImageField(upload_to = "images/", default = "images/user_default.jpg")

	def __str__(self):
		return str(self.user)

class Entrepreneur(models.Model):
	user      = models.OneToOneField(User)
	status    = models.CharField(max_length = 50, choices = STATUS)
	location  = models.ForeignKey('Location', null = True, blank = True)
	address   = models.CharField(max_length = 100, blank = True)
	price     = models.IntegerField(default = 0)
	telephone = models.CharField(max_length = 100, blank = True)
	addition  = models.CharField(max_length = 500, blank = True)
	about     = models.CharField(max_length = 500, default = "Предприниматель")

	photo     = models.ImageField(upload_to = "images/", default = "images/home_default.jpg")

	checked   = models.BooleanField(default = False)

	birthday        = models.DateField(default = "2001-04-04")
	sex             = models.BooleanField(default = False, choices = SEX)
	passport_series = models.CharField(max_length = 4)
	passport_number = models.CharField(max_length = 6)
	unit_code 		= models.CharField(max_length = 7)

	def __str__(self):
		return str(self.user)

class Administrator(models.Model):
	user      = models.OneToOneField(User)
	checked   = models.BooleanField(default = False)
	location  = models.ForeignKey('Location')
	about     = models.CharField(max_length = 500, default = "Администрация")
	telephone = models.CharField(max_length = 100, default = "Не скажу :)")
	address   = models.CharField(max_length = 100, default = "")
	photo     = models.ImageField(upload_to = "images/", default = "images/administrator_default.jpg")

	checked   = models.BooleanField(default = False)

	birthday        = models.DateField(default = "2001-04-04")
	sex             = models.BooleanField(default = False, choices = SEX)
	passport_series = models.CharField(max_length = 4)
	passport_number = models.CharField(max_length = 6)
	unit_code 		= models.CharField(max_length = 7)
	def __str__(self):
		return str(self.user)

class Location(models.Model):
	location = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.location)