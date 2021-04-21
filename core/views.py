from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    user = request.user
    return render(request,'home.html',locals())