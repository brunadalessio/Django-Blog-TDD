from django.shortcuts import render
from .models import Postagem

def home(request):
    posts = Postagem.objects.all()
    context = {"posts":posts}
    return render(request, 'main/home.html', context)