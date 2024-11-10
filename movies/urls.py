from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name="list"),
    path('<slug:slug>', views.movie_page, name="page"),
    path('new-movie/', views.new_movie, name='new-movie'),
]