from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Judge

def judges(request: HttpRequest) -> HttpResponse:
    judges = Judge.objects.all()
    return render(request, "judges.html", dict(judges=judges))
