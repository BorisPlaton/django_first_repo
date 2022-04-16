from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Person


def create_person(request):
    if request.POST:
        Person.objects.create(name=request.POST['name'], age=request.POST['age'])
        return redirect(reverse('people:create_persons'))
    return render(request, "people/create_person.html")


def delete_person(request):
    if request.POST:
        Person.objects.get(pk=request.POST["pk"]).delete()
        return redirect(reverse('people:delete_person'))
    return render(request, "people/delete_person.html")


def view_persons(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, "people/view_persons.html", context=context)


def index(request):
    return redirect(reverse('people:view_persons'))
