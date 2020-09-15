from django.urls import path, include
from articles.views import PostsListView, PostDetailView

urlpatterns = [
    path('', PostsListView.as_view(), name='list'),
    path('<pk>/', PostDetailView.as_view())
]

