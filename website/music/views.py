from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def music(request):
    if request.user.is_authenticated():
        movies = models.movielist.objects.all()
        return render(request,'musico/home.html',{'movie_list':movies})
    else:
        return HttpResponse("You need user access")
def listsong(request,pk):
    movie = models.movielist.objects.get(pk=pk)
    return render(request,'musico/list.html',{'album':movie})