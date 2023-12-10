from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector
from .models import MusicStyle, Contestant
from teacher.models import Teacher
from judge.models import Judge
from .forms import SearchForm
from itertools import chain
from django.contrib.postgres.search import TrigramSimilarity


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def contestants(request: HttpRequest) -> HttpResponse:
    contestants = Contestant.objects.all()
    return render(request, "contestants.html", dict(contestants=contestants))


def contestant_detail(request: HttpRequest, contestant_slug: str) -> HttpResponse:
    contestant = Contestant.objects.get(slug=contestant_slug)
    return render(request, "contestant_detail.html", dict(contestant=contestant))


# def get_similarity_queryset(model, fields, query):
#     return model.objects.annotate(
#         similarity=sum(TrigramSimilarity(field, query) for field in fields)
#     ).filter(similarity__gt=0.3)


# def search(request: HttpRequest) -> HttpResponse:
#     query = request.GET.get("input", "").lower()
#     contestants = get_similarity_queryset(
#         Contestant, ["first_name", "music_style__name"], query
#     )
#     teachers = get_similarity_queryset(Teacher, ["first_name"], query)
#     judges = get_similarity_queryset(Judge, ["first_name"], query)
#     results = chain(contestants, teachers, judges)
#     return render(request, "search.html", dict(query=query, results=results))


def search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("input", "").lower()
    contestants = Contestant.objects.annotate(
        search=SearchVector("first_name", "music_style__name")
    ).filter(search=query)
    teachers = Teacher.objects.annotate(
        search=SearchVector("first_name", "last_name")
    ).filter(search=query)
    judges = Judge.objects.annotate(
        search=SearchVector("first_name", "last_name")
    ).filter(search=query)
    results = chain(contestants, teachers, judges)
    return render(request, "search.html", dict(query=query, results=results))
