from django.shortcuts import render
from .models import Resource

def resources(request):
    resources_list = Resource.objects.all()
    context = {"resources_list": resources_list}
    return render(request, "recomendations/all_resources.html", context)
