from django.shortcuts import render, redirect
from .models import Movies
from . import forms

# Create your views here.

def movies_list(request):
    movies = Movies.objects.all().order_by('date')
    return render(request, 'movies/movies_list.html', {'movies': movies})

def movie_page(request, slug):
    movie = Movies.objects.get(slug=slug)
    return render(request, 'movies/movie_page.html', {'movies': movie})

def new_movie(request):
    if request.method == 'POST':
        form = forms.CreateMovie(request.POST, request.FILES)
        if form.is_valid():
            newMovie = form.save(commit=False)
            newMovie.user = request.user
            newMovie.save()
            return redirect('movies:list')
    else:
        form = forms.CreateMovie()
        
    return render(request, 'movies/new_movie.html', { 'form': form })