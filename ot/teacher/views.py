from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def teacher_list(request: HttpRequest) -> HttpResponse:
    return render(request, "list.html")
