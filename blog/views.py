from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, 'blog/article_page.html', {'article' : article})


def edit_page(request):
    return render(request, 'blog/edit_page.html')


@csrf_exempt
def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    if len(title.strip()) > 0 and len(content.strip()) > 0:
        models.Article.objects.create(title=title, content=content)
    return redirect('blog:home')
