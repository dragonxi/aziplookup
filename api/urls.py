from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ip/lookup", views.lookup, name="ip_lookup"),
]
