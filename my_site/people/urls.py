from django.urls import path

from . import views

app_name = 'people'

urlpatterns = [
    path("view_persons/", view=views.view_persons, name="view_persons"),
    path("create_person/", view=views.create_person, name="create_persons"),
    path("delete_person/", view=views.delete_person, name="delete_person"),
    path("", view=views.index, name="index")
]
