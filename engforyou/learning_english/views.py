from lib2to3.fixes.fix_input import context
from pydoc_data.topics import topics


from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from .models import Topic, Lesson, SpeakingTheme, Verb, Comment
from .forms import CommentForm

import random

def random_url(request):
    urls = ['topics', 'lessons', 'about', 'speaking', 'verbs', 'times']
    random_url = random.choice(urls)
    return redirect(reverse(random_url))


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
    comments = Comment.objects.filter(topic=topic).order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return redirect(reverse('detail_topic', args=[pk]))
    else:
        comment_form = CommentForm()
    return render(request, 'learning_english/topic.html',
                  {'topic': topic,
                   'topic_id':topic.id,
                   'comments': comments, 
                   'form': comment_form})
    


def lessons(request):
    lessons_list = Lesson.objects.all()
    context = {"lessons_list": lessons_list}
    return render(request, "learning_english/lessons.html", context)

def detail_lesson(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    comments = Comment.objects.filter(lesson=lesson).order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.lesson = lesson
            comment.save()
            return redirect(reverse('detail_lesson', args=[pk]))
    else:
        comment_form = CommentForm()
    return render(request, 'learning_english/lesson.html',
                  {'lesson': lesson,
                   'lesson_id':lesson.id,
                   'comments': comments, 
                   'form': comment_form})

def detail(request, topic_id):
    return HttpResponse("You're looking at topic %s." % topic_id)




@login_required
def add_comment(request, lesson_id=None, topic_id=None):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            if lesson_id:
                comment.lesson_id = lesson_id
            if topic_id:
                comment.topic_id = topic_id
            comment.save()
            return redirect('detail_lesson' if lesson_id else 'detail_topic')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})
