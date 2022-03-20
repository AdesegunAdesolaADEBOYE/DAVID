from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def cv(request):
    return render(request, "event.html")

    