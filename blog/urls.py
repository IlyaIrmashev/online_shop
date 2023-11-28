from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='article_list'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('article/<slug:slug>/', BlogDetailView.as_view(), name='article_slug'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
