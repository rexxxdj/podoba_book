from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import *
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
	#students urls
	url(r'^$','students.views.students.students_list',name='home'),
	url(r'^students/add/$','students.views.students.students_add',name='students_add'),
	url(r'^students/(?P<sid>\d+)/edit/$','students.views.students.students_edit',name='students_edit'),
	url(r'^students/(?P<sid>\d+)/delete/$','students.views.students.students_delete',name='students_delete'),

	#Groups urls
	url(r'^groups/$','students.views.groups.groups_list',name='groups'),
	url(r'^groups/add/$', 'students.views.groups.groups_add',name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$','students.views.groups.groups_edit',name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$','students.views.groups.groups_delete',name='groups_delete'),

	#Attendance urls
	url(r'^attendance/$','students.views.attendance.attendance',name='attendance'),
	url(r'^attendance/(?P<sid>\d+)$','students.views.attendance.attendance_edit',name='attendance_edit'),

    url(r'^admin/', admin.site.urls),
]

if DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': MEDIA_ROOT}))