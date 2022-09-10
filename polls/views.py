from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def contact(request):
    return HttpResponse("Contact Page")


def home(request):
    return HttpResponse("Home Page")
