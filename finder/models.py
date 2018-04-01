# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hostels(models.Model) :
	HostelName = models.CharField(max_length=20,default='Select your Hostel',null=False)

	def __unicode__(self):
		return unicode(self.HostelName)


class Status(models.Model):
	StudentStatus = models.CharField(max_length=20,default=None,null=False)

	def __unicode__(self):
		return unicode(self.StudentStatus)

class Movie:
	L_Choices = (
		('eng' , 'eng'),
		('esp' , 'esp'),
		('hin' , 'hin'),
		('fre' , 'fre'),
	)
	m_title = models.CharField(max_length = 100 , default = None, null = False)
	m_lang = models.CharField(max_length = 100 , default = 'eng' ,choices = L_Choices , null = False)
	m_year = models.CharField(max_length = 200 , default = None, null = False)
	m_url = models.CharField(max_length = 2000,default = None)
	m_dir = models.CharField(max_length = 200)
	m_uvote = models.IntegerField(default = 120)
	m_rvote = models.IntegerField(default = 20)
	m_urating = models.FloatField(default = 10 , null = False)
	m_rrating = models.FloatField(default = 100, null = False)
	def __unicode__(self):
		return unicode(m_title)

class UserMovies(models.Model):
	u_id = models.IntegerField(null = False)
	u_movie_id = models.IntegerField(null = False)
	u_rating = models.FloatField(default = 10, null = False)

	#def __unicode__(self):
	#	return unicode(self.u_movie_id)

class Student(models.Model) :
	G_Choices = (
		('action','action') ,
		('romance','romance'),
		('comedy','comedy'),
		('crime' , 'crime'),
		('horror' , 'horror'),
		('sci-fi' , 'sci-fi'),
	)
	name = models.CharField(max_length=50,default=None,null=False, primary_key = True)
	RollNo = models.CharField(max_length=20,default=None,null=False)
	hostel = models.ForeignKey(Hostels,default=None,null=False)
	status = models.ForeignKey(Status,default=None,null=False)
	Genre1 = models.CharField(max_length = 20, default = 'Action' ,choices = G_Choices , null = False)
	Genre2 = models.CharField(max_length = 20, default = 'Romance' ,choices = G_Choices , null = False)
	Genre3 = models.CharField(max_length = 20, default = 'Thriller' ,choices = G_Choices , null = False)
	def __unicode__(self):
		return unicode(self.name)
