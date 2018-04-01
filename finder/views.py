# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from models import Student,Hostels,Status
from django.views.generic import View
from forms import StudentForm
from django.shortcuts import redirect
# from forms import StudentForm

# Create your views here.
def login(request):
	all_students = Student.objects.all()
	return render(request,'login.html',{'all_students' : all_students})
def index(request) :
	form = StudentForm(request.POST)
	if(request.method=='POST'):
		if(form.is_valid()):
			form.save()
			stu = Student.objects.all()
			UserList = User.objects.all()
			for tm in stu:
				f = 0
				for che in UserList:
					if (tm.name == che.username):
						f = 1
						break
				if f==0:
					user = User.objects.create_user(username = tm.name,
													password = tm.RollNo,
													email = 'tm@gmail.com'
													)

			#print form.cleaned_data[Student.name]
			#user = User.objects.create_user(username = {{form.name}}, 
			#								password = {{form.RollNo}},
			#								email = 'tm@gmail.com'
			#								)
			message = 'Successfully Registered'
			#return render(request,'login.html',{'message': message})
			return redirect("/", {'message' : message})

		else :
			form_error = "(Registration Failed. Username Exists?)"
			return render(request,'index.html',{'form': form,'form_error': form_error})
	else :
		form = StudentForm(request.POST)
	return render(request,'index.html',{'form': form})

def details(request):
	object_list = Student.objects.all().order_by('status_id')
	bh1 = Student.objects.filter(hostel__id=1).order_by('status_id')
	bh2 = Student.objects.filter(hostel__id=2).order_by('status_id')
	bh3 = Student.objects.filter(hostel__id=3).order_by('status_id')
	bh4 = Student.objects.filter(hostel__id=4).order_by('status_id')
	gh1 = Student.objects.filter(hostel_id=5).order_by('status_id')
	gh2 = Student.objects.filter(hostel_id=6).order_by('status_id')

	return render(request,'detail.html',{'object_list':object_list,'bh1': bh1,'bh2': bh2,'bh3': bh3,'bh4': bh4,'gh1': gh1,'gh2': gh2,})

def home(request):
	alb = Student.objects.all()
	tm = 'NULL'
	if request.user.is_authenticated():
		tm = user.username
	return render(request , 'home.html' , {'alb' : alb , 'tm' : tm})