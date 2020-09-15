from django.shortcuts import get_object_or_404, render


from articles.models import Article
from django.views.generic import ListView, DetailView


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_list.html', {'article': article})


class PostsListView(ListView):
    model = Article


class PostDetailView(DetailView):
    model = Article

