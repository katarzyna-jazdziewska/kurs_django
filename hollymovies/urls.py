"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viewer.views import hello, movies, MoviesView, MovieCreateView, MovieUpdateView, MovieDeleteView, MovieDetailsView

# hello jest funkcją i wywołujemy to normalnie, a moviesView i MoviesCreateView są klasami dlatego wywyołujemy jako widok

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    path('movie/', MoviesView.as_view(), name="filmy"),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name="movie_details"),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
]

# CRUD
# C create
# R read (List, Retrive)
# U update
# D delete