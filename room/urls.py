from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("rooms/", views.rooms, name="rooms"),
    path("payment_completed/", views.payment_done, name="payment"),
]