from .views import classify_message, dashboard
from django.urls import path
urlpatterns = [
    path("", classify_message, name=""),
    path("dashboard/", dashboard, name="dashboard"),
]
