from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import MusicStyle, Contestant
from .forms import SearchForm

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def contestants(request: HttpRequest) -> HttpResponse:
    contestants = Contestant.objects.all()
    return render(request, "contestants.html", dict(contestants=contestants))

def contestant_detail(request: HttpRequest, contestant_slug: str) -> HttpResponse:
    contestant = Contestant.objects.get(slug=contestant_slug)
    return render(request, "contestant_detail.html", dict(contestant=contestant))

def search(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            contestants = Contestant.objects.filter(first_name__icontains=search)
            return render(
                request, "contestants.html", dict(contestants=contestants, search=search)
            )
    else:
        form = SearchForm()
    return render(request, "search.html", dict(form=form, contestants=contestants))