from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def teachers(request: HttpRequest) -> HttpResponse:
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", dict(teachers=teachers))


def teacher_detail(request: HttpRequest, teacher_slug: str) -> HttpResponse:
    teacher = get_object_or_404(Teacher, slug=teacher_slug)
    return render(request, "teacher_detail.html", dict(teacher=teacher))
