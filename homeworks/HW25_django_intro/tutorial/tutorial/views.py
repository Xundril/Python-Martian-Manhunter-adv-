from django.http import HttpResponse
from .extra_task import color_generator


def status(request):
    return HttpResponse("OK")


def color(request):
    response = f'<center><h1 style="color:{color_generator()};">Color: {color_generator()}</h1></center>'
    return HttpResponse(response)
