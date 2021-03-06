from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Person
from .forms import CreatePersonForm, DeletePersonForm


def create_person(request):
    form = CreatePersonForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('people:create_persons'))
    return render(request, "people/create_person.html", context={"form": form})


def delete_person(request):
    form = DeletePersonForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.POST:
        if form.is_valid():
            Person.objects.get(pk=form.cleaned_data.get("person")).delete()
            return redirect(reverse('people:delete_person'))
    return render(request, "people/delete_person.html", context=context)


def view_persons(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, "people/view_persons.html", context=context)


def index(request):
    return redirect(reverse('people:view_persons'))
