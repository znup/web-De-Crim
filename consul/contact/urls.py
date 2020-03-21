from django.urls import path
from . import views

urlpatterns = [
    #paths de contact
    path('', views.contact, name="contact"),
]