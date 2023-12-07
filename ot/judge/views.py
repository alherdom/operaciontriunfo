from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Judge


def judges(request: HttpRequest) -> HttpResponse:
    judges = Judge.objects.all()
    return render(request, "judges.html", dict(judges=judges))


def judge_detail(request: HttpRequest, judge_slug: str) -> HttpResponse:
    judge = get_object_or_404(Judge, slug=judge_slug)
    return render(request, "judge_detail.html", dict(judge=judge))
