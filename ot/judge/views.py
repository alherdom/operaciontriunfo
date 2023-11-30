from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def judge_list(request: HttpRequest) -> HttpResponse:
    return render(request, "list.html")
