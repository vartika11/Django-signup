from django.shortcuts import render
from django.http import HttpResponse
from .models import Login


# Create your views here.
def index (request):
    logins = Login.objects.all()
    return render(request, 'index.html', {'logins': logins})
   # return HttpResponse('Hello')




