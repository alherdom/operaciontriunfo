from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import MusicStyle, Contestant


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def contestants(request: HttpRequest) -> HttpResponse:
    contestants = Contestant.objects.all()
    return render(request, "contestants.html", dict(contestants=contestants))

def contestant_detail(request: HttpRequest, contestant_slug: str) -> HttpResponse:
    contestant = Contestant.objects.get(slug=contestant_slug)
    return render(request, "contestant_detail.html", dict(contestant=contestant))