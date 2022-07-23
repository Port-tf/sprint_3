from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Author, Poem, User


def default(request):
    return HttpResponse(
        '<h1>Разработчик пока непридумал, что будет по этому адресу, '
        'поэтому просто вывел это сообщение</h1>'
    )

def index_1(request):    
    return render(request, 'posts/index_1.html')

def index_2(request):    
    return render(request, 'posts/index_2.html')


def poems(request):
    poems = Poem.objects.all()
    context = {
       'poems': poems,
    }
    return render(request, 'posts/poems.html', context)

def poem_author(request, web_name):
    author = get_object_or_404(Author, name_url=web_name)
    poems = author.poems.all()  # .first()
    context = {
        'author': author,
        'poems': poems,
    }
    return render(request, 'posts/poem_author.html', context)

def post_detail(request, argument_id):
    poem = get_object_or_404(Poem, pk=argument_id)
    context = {
        'poem': poem,
    }
    return render(request, 'posts/poem_detail.html', context)

def poem_user(request, user_name):
    user = get_object_or_404(User, username=user_name)
    poems = user.poems.all()  # .first()
    context = {
        'user': user,
        'poems': poems,
    }
    return render(request, 'posts/poem_user.html', context)
