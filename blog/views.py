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


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/edit_page.html', {'article': article})


@csrf_exempt
def edit_action(request):
    article_id = request.POST.get('article_id',  '0')
    print('article_id', article_id)
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    if article_id == '0':
        if len(title.strip()) > 0 and len(content.strip()) > 0:
            models.Article.objects.create(title=title, content=content)
            return redirect('blog:home')
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})
