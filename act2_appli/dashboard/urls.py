from django.urls import path
from .views import index, dashboard

app_name = "dashboard"

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
]
