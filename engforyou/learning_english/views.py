from lib2to3.fixes.fix_input import context
from pydoc_data.topics import topics

from django.http import HttpResponse
from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "learning_english/index.html", context)

def about(request):
    return render(request, "learning_english/about.html")

def topics(request):
    
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "learning_english/topics.html", context)

def detail(request, topic_id):
    return HttpResponse("You're looking at topic %s." % topic_id)
