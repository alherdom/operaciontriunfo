from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def teachers(request: HttpRequest) -> HttpResponse:
    return render(request, "teachers.html")
