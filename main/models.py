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

class Admin_Request(models.Model):
	administrator = models.OneToOneField('Administrator',on_delete=models.CASCADE)
	location      = models.ForeignKey('Location',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.administrator)
		
class Entr_Request(models.Model):
	entrepreneur  = models.OneToOneField('Entrepreneur', null = True,on_delete=models.CASCADE)
	administrator = models.ForeignKey('Administrator', null = True,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.entrepreneur) + " " +str(self.administrator)

class Point(models.Model):
	consumer     = models.ForeignKey('Consumer',on_delete=models.CASCADE)
	entrepreneur = models.ForeignKey('Entrepreneur',on_delete=models.CASCADE)
	point        = models.IntegerField(default = 0)
	date         = models.DateField(default = timezone.now())

	def __str__(self):
		return str(self.consumer) + ' ' + str(self.entrepreneur)

class Consumer_Request(models.Model):
	consumer     = models.ForeignKey('Consumer',on_delete=models.CASCADE)
	entrepreneur = models.ForeignKey('Entrepreneur',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.consumer) + " " + str(self.entrepreneur)
		
class Filter(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	price    = models.IntegerField(default = 0)
	repair   = models.BooleanField(default = False)
	home     = models.BooleanField(default = False)
	location = models.ForeignKey('Location', null = True, blank = True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user) + " filters"

class Consumer(models.Model):
	user      = models.OneToOneField(User,on_delete=models.CASCADE)
	rate      = models.CharField(max_length = 50,default = "Beginner", choices = RATE)

	telephone = models.CharField(max_length = 100,default = "Ни скажу!")
	age       = models.IntegerField(default = 18)
	wishes    = models.CharField(max_length = 100, default = "Все не почём!")

	photo     = models.ImageField(upload_to = "images/", default = "images/user_default.jpg")

	def __str__(self):
		return str(self.user)

class Entrepreneur(models.Model):
	user      = models.OneToOneField(User,on_delete=models.CASCADE)
	status    = models.CharField(max_length = 50, choices = STATUS)

	location  = models.ForeignKey('Location', null = True, blank = True,on_delete=models.CASCADE)
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
	user      = models.OneToOneField(User,on_delete=models.CASCADE)
	checked   = models.BooleanField(default = False)
	location  = models.ForeignKey('Location',on_delete=models.CASCADE)
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
