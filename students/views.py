from django.shortcuts import render
from django.http import HttpResponse


#students
def students_list(request):
	students = (
		{'id': 1,
		'first_name': u'Ruslan',
		'last_name': u'Tokar',
		'ticket': 235,
		'image': 'img/test.jpg'},
		{'id': 2,
		'first_name': u'Povazhnuk',
		'last_name': u'Serhyi',
		'ticket': 2123,
		'image': 'img/test.jpg'},
	)
	return render(request,'students/students_list.html',{'students':students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)


#groups
def groups_list(request):
	return render(request,'students/groups_list.html')

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
	
#attendance
def attendance(request):
	return render(request,'students/attendance.html')

def attendance_edit(request,sid):
	return render(request,'students/attendance.html')
