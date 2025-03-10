from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.greet,  name="greet"),
    path("dimi", views.dimi, name='dimi'),
    path("nat", views.nat, name='nat')
]