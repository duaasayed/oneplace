from django.urls import path
from . import views

app_name = 'scrapping'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('results', views.results, name='results')
]