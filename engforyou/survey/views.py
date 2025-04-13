from django.shortcuts import render

def survey_view(request):
    return render(request, 'survey/survey.html')
