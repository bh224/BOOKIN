from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_all, name='search-all'),
]
