from django.shortcuts import render
from .  import models


def index(request):
    return render(request, 'moderator/dashboard.html')

def moderator_dahsboard(request,user):
    alluser = models.CustomUser.objects.all()
    allpublication = models.Publication.objects.all()
    
    return render(request, 'moderator/dashboard.html', {'alluser':alluser, 'allpublication':allpublication})