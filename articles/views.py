from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,

    }
    return render(request, 'create.html', context)

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id = id)
    context = {
        'article': article,
    }

    return render(request, 'detail.html', context)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article) # (들어온 정보, 기존 정보(id를 위해))
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id) # id를 넣어서 디테일 페이지로 들어가게
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')