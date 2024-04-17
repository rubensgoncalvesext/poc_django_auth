from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    breakpoint()
    username = request.user.username if request.user.is_authenticated else 'Anonymous'
    return HttpResponse(f"Hello, {username}!")

