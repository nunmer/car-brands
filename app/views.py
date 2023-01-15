from django.shortcuts import render
from .models import Cars

# Create your views here.
def index(request):
    obj=Cars.objects.all()
    context={
        "obj": obj,
    }
    return render(request, "index.html", context)