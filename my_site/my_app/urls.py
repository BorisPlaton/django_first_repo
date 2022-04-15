from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path("<int:num>", views.num_topic, name='num_topic'),
    path("<str:topic>/", views.topics, name='topic'),
    path("", views.index, name="index"),
]

