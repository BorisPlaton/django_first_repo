from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

articles = {
    "sport": "sports articles",
    "finance": "finance articles",
    "food": "food articles",
}


# Create your views here.
def topics(request, topic):
    try:
        return HttpResponse(articles[topic])
    except KeyError:
        raise Http404(f"No topic {topic}")


def num_topic(request, num):
    try:
        topic = list(articles.keys())[num]
        return HttpResponseRedirect(reverse('topic', args=[topic]))
    except IndexError:
        raise Http404(f"Wrong num")


def index(request):
    return render(request, "my_app/index.html")
