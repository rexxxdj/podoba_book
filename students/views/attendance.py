# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from ..models import group

#attendance
def attendance(request):
	return render(request,'students/attendance.html')

def attendance_edit(request,sid):
	return render(request,'students/attendance.html')