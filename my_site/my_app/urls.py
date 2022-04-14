from django.urls import path
from . import views

urlpatterns = [
    path("<int:num>", views.num_topic, name='num_topic'),
    path("<str:topic>/", views.index, name='index'),
]

