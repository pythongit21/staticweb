from django.shortcuts import render

from .models import place, person


# Create your views here.
def homepg(request):
    pl = place.objects.all()
    pr = person.objects.all()
    return render(request, "index.html", {'plc': pl, 'per': pr})