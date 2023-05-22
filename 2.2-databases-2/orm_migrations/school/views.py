from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    all_students = Student.objects.order_by('group')
    context = {
        'students': all_students
    }
    return render(request, template, context)
