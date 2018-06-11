from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
# Create your views here.

def movie(request):
	return HttpResponse("movies will be displayed here")


class list(generic.ListView):
	model=models.song
	context_object_name = 'movie_list'
	template_name = 'movie/sample.html'

def detail(request,pk):
	movie=models.movielist.objects.get(pk=pk)
	return render(request, 'movie/detailview.html' ,{'movie':movie})

