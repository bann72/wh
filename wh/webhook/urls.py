from django.urls import path
from . import views

urlpatterns = [
    path("", views.webhook_handler, name="webhook_handler"),
]