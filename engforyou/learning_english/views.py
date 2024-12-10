from lib2to3.fixes.fix_input import context
from pydoc_data.topics import topics

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from .models import Topic, Lesson, SpeakingTheme, Verb

import random

def random_url(request):
    urls = ['topics', 'lessons', 'about', 'speaking', 'verbs', 'times']
    random_url = random.choice(urls)
    return redirect(reverse(random_url))

# Create your views here.
def index(request):
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "learning_english/index.html", context)

def about(request):
    return render(request, "learning_english/about.html")

def times(request):
    return render(request, "learning_english/times.html")

def verbs(request):
    verbs_list = Verb.objects.all()
    context = {"verbs_list": verbs_list}
    return render(request, "learning_english/verbs.html", context)
    

def speaking(request):
    speaking_list = SpeakingTheme.objects.all()
    random_theme = SpeakingTheme.objects.order_by('?')[0]
    context = {"speaking_list": speaking_list, "random_theme": random_theme}
    return render(request, "learning_english/speaking.html", context)

def topics(request):
    topics_list = Topic.objects.all()
    context = {"topics_list": topics_list}
    return render(request, "learning_english/topics.html", context)

def detail_topic(request, pk):
    topic = Topic.objects.get(pk=pk)
    return render(request, 'learning_english/topic.html', {'topic': topic})


def lessons(request):
    lessons_list = Lesson.objects.all()
    context = {"lessons_list": lessons_list}
    return render(request, "learning_english/lessons.html", context)

def detail_lesson(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    return render(request, 'learning_english/lesson.html', {'lesson': lesson})

def detail(request, topic_id):
    return HttpResponse("You're looking at topic %s." % topic_id)
