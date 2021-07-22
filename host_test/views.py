from django.http import JsonResponse

def country(request):
    data = {'country': 'Ghana'}
    return JsonResponse(data)
    