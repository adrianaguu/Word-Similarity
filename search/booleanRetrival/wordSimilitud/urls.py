from django.urls import path
from . import views

urlpatterns = [
    path('', views.calulateSimilarity, name='calulate_simility'),
]