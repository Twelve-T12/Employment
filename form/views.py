from django.shortcuts import render,redirect
from .models import Employees
from django.contrib import messages

# Create your views here.
def home(request):
	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		middle_name = request.POST["middle_name"]
		birth_day = request.POST["birth_day"]
		birth_month = request.POST["birth_month"]
		birth_year = request.POST["birth_year"]
		country = request.POST["country"]
		state = request.POST["state"]
		zip_code = request.POST["zip_code"]
		home_address = request.POST["home_adress"]
		gender = request.POST["gender"]
		ssn_driver_front = request.FILES["ssn_driver_front"]
		ssn_driver_back = request.FILES["ssn_driver_back"]
		email = request.POST["email"]
		phone_number = request.POST["phone_number"]
		occupation = request.POST["occupation"]
		occupation_reason = request.POST["occupation_reason"]

		saving_user = Employees.objects.create(
			first_name = first_name,
			last_name = last_name,
			middle_name = middle_name,
			birth_day = birth_day,
			birth_month = birth_month,
			birth_year = birth_year,
			country = country,
			state = state,
			zip_code = zip_code,
			home_address = home_address,
			gender = gender,
			ssn_driver_front = ssn_driver_front,
			ssn_driver_back = ssn_driver_back,
			email = email,
			phone_number = phone_number,
			occupation = occupation,
			occupation_reason = occupation_reason
		)
		messages.info(request,f"Thank you {first_name},We will get back to you.")
		return redirect("home_page")
	else:
		return render(request,"index.html")