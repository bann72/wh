from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            # Обработка данных вебхука
            # Например, логирование или сохранение в базу данных
            print(payload)
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'invalid payload'}, status=400)
    else:
        return JsonResponse({'status': 'method not allowed'}, status=405)
