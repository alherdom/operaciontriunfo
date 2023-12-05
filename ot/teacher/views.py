from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Teacher


def teachers(request: HttpRequest) -> HttpResponse:
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", dict(teachers=teachers))
