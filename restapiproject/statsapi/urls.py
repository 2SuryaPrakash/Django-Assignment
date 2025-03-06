from django.urls import path

from . import views
app_name = "statsapi"
urlpatterns = [
    path('', views.placement_statistics, name="statistics"),
    
]