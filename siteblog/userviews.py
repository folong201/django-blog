from django.shortcuts import render 
from . import models



def index(request):
    return render(request, 'user/index.html')

def userdashboard(request,user):
    user = models.CustomUser.objects.get(username=user.username)
    publications = models.Publication.objects.filter(author=user)
    articles = models.Article.objects.filter(author=user)
    
    return render(request, 'user/author.html', {'user':user, 'publications':publications, 'articles':articles})
    