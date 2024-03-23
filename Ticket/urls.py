from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ticket_view, name='Ticket'),
]
