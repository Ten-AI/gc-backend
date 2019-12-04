from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import logging


@csrf_exempt
def image_classify(request):
    """ Image classification """

    if request.method == 'POST':
        # Get upload image
        img = request.FILES.get('img', None)
        if img:
            return JsonResponse(dict(name=img.name, size=img.size))
        else:
            return JsonResponse(dict(code=401, msg='Bad request'))

