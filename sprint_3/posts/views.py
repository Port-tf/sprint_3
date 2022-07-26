from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Author, Biografy, Poem, User


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
        'poemsis': poems,
    }
    return render(request, 'posts/poem_user.html', context)

def biografy(request, name):
    biografy = get_object_or_404(Biografy, name=name)
    poem_last = biografy.bio.poems.last()
    # poem_last = Author.objects.get(id=biografy.bio.id).poems.last()
    context = {
        'user': biografy,
        'poem': poem_last,
    }
    return render(request, 'posts/biografy.html', context)