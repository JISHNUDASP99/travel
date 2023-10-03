from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    tem=team.objects.all()
    return render(request,"index.html",{'result':obj,'res':tem})

# def login(request):
#     return render(request, "login1.html")
# def con(request):
#     return HttpResponse("login successfully")