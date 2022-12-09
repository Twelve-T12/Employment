from django.db import models

# Create your models here.

class Employees(models.Model):
	first_name = models.CharField(max_length=1000,default=True)
	last_name = models.CharField(max_length=1000,default=True)
	middle_name = models.CharField(max_length=1000,default=True)
	birth_day = models.CharField(max_length=1000,default=True)
	birth_month = models.CharField(max_length=1000,default=True)
	birth_year = models.CharField(max_length=1000,default=True)
	country = models.CharField(max_length=1000,default=True)
	state = models.CharField(max_length=1000,default=True)
	zip_code =  models.CharField(max_length=1000,default=True)
	home_address =  models.CharField(max_length=1000,default=True)
	gender = models.CharField(max_length=1000,default=True)
	ssn_driver_front = models.FileField(upload_to="all_snn_driver_front",default=True)
	ssn_driver_back = models.FileField(upload_to="all_ssn_driver_back",default=True)
	email = models.CharField(max_length=1000,default=True)
	phone_number = models.CharField(max_length=1000,default=True)
	occupation = models.CharField(max_length=1000,default=True)
	occupation_reason = models.CharField(max_length=1000,default=True)
	
	def __str__(self):
		return self.country