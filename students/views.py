from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Student


#students
def students_list(request):
	students = Student.objects.all().order_by('last_name')
	order_by = request.GET.get('order_by', '')
	if order_by in ('photo','last_name','first_name','ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse','') == '1':
			students = students.reverse()

	paginator = Paginator(students,2)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
		students = paginator.page(paginator.num_pages)

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
