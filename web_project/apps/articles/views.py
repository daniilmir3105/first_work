# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse('Hello world!')

# def test(request):
#     return HttpResponse('This is test!')

from django.shortcuts import render
from . import models
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

Article = models.Article
Comment = models.Comment

def index(request):
    latest_articles_list = Article.objects.order_by('-public_date')[:5] # последние 5 статей возвращаем
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id): # при помощи этой функции будем выводить статьи 
    try: 
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Article not found')

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try: 
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Article not found')

    # return render(request, 'articles/detail.html', {'article': a})
    a.comment_set.create(autor_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))