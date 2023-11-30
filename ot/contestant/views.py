from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import MusicStyle, Contestant

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")