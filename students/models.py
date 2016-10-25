# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Student(models.Model):

	class Meta(object):
		verbose_name = 'Student',
		verbose_name_plural = 'Students'

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)

	first_name = models.CharField(
		max_length=256,
		blank = False,
		verbose_name='Name')

	last_name = models.CharField(
		max_length = 256,
		blank = True,
		verbose_name ='SurName')

	middle_name = models.CharField(
		max_length = 256,
		blank = True,
		verbose_name='FathersName',
		default = '')

	birthday = models.DateField(
		blank = False,
		verbose_name = 'Birthday Date',
		null = True)

	photo = models.ImageField(
		blank = True,
		verbose_name = 'Photo',
		null=True)

	ticket = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = 'Ticket')

	notes = models.TextField(
		blank = True,
		verbose_name = 'More info')

	student_group = models.ForeignKey('Group',
		verbose_name = 'Group',
		blank = False,
		null = True,
		on_delete = models.PROTECT)


class Group(models.Model):

	class Meta(object):
		verbose_name = 'Group'
		verbose_name_plural = 'Groups'

	title = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = 'Name')

	leader = models.OneToOneField('Student',
		verbose_name = 'Leader',
		blank = True,
		null = True,
		on_delete = models.SET_NULL)

	notes = models.TextField(
		blank = True,
		verbose_name = 'More notes...')

	def __unicode__(self):
		if self.leader:
			return '%s (%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
		else:
			return '%s' % (self.title,)