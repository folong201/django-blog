from django.shortcuts import render

# Create your views here.


def index(request):
    articlelist = [
        {
            'id': 1,
            'title': 'Hello World',
            'content': 'This is the first article of our blog site.'
        },
        {
            'id': 2,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        }
    ]
    publicationlist = [
        {
            'id': 1,
            'title': 'Hello World',
            'content': 'This is the first article of our blog site.'
        },
        {
            'id': 2,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 3,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 4,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 5,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 6,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 7,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 8,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 9,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 10,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 11,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 12,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 13,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 14,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 15,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 16,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 17,
            'title': 'Hello Django',
            'content': 'This'},
    ]
    return render(request, 'index.html', {'articlelist': articlelist})

def all_article(request):
    articlelist = [
        {
            'id': 1,
            'title': 'Hello World',
            'content': 'This is the first article of our blog site.'
        },
        {
            'id': 2,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        }
    ]
    return render(request, 'all_article.html', {'articlelist': articlelist})

def all_publication(request):
    publicationlist = [
        {
            'id': 1,
            'title': 'Hello World',
            'content': 'This is the first article of our blog site.'
        },
        {
            'id': 2,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 3,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 4,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 5,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 6,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 7,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 8,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 9,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 10,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 11,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 12,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 13,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },
        {
            'id': 14,
            'title': 'Hello Django',
            'content': 'This is the second article of our blog site.'
        },]
    
    return render(request, 'all_publication.html', {'publicationlist': publicationlist})

def article_detail(request, article_id):
    article = {
        'id': 1,
        'title': 'Hello World',
        'content': 'This is the first article of our blog site.'
    }
    return render(request, 'article_detail.html', {'article': article})

def publication_details(request):
    publication = {
        'id': 1,
        'title': 'Hello World',
        'content': 'This is the first article of our blog site.'
    }
    return render(request, 'publication_details.html', {'publication': publication})