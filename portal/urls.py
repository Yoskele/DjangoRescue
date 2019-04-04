from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
	path('', views.index, name='index'),
    # to do: add more paths...
    path('persons/add/', views.add_person, name='add_person'),
]