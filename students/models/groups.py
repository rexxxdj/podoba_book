# -*- coding: utf-8 -*-

from django.db import models

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