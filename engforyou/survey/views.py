from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import LearningStyle

def survey_view(request):
    return render(request, 'survey/survey.html')

def save_learning_profile(request):
    if request.method == 'POST':
        try:
            data = request.POST
            data_ = dict(data.lists())
            data_.pop('csrfmiddlewaretoken')
            user = request.user
            LearningStyle.objects.update_or_create(
                user=user,
                defaults={
                    'visual_percent': data['visual_percent'],
                    'audio_percent': data['audio_percent'],
                    'reader_percent': data['reader_percent'],
                    'kinesthetic_percent': data['kinesthetic_percent'],
                    'primary_style': data['primary_style'],
                    'secondary_style': data['secondary_style']
                }
)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Профиль успешно сохранен'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'}, status=405)