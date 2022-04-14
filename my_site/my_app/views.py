from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    "sport": "sports articles",
    "finance": "finance articles",
    "food": "food articles",
}


# Create your views here.
def index(request, topic):
    result = articles.get(topic)
    try:
        return HttpResponse(articles[topic])
    except KeyError:
        raise Http404(f"No topic {topic}")


def num_topic(request, num):
    try:
        topic = list(articles.keys())[num]
        return HttpResponseRedirect(reverse('index', args=[topic]))
    except IndexError:
        raise Http404(f"Wrong num")
