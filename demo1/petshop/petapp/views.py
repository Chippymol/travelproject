from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Teammember


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj2 = Teammember.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj2})
