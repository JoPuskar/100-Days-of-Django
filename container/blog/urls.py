from django.urls import path

from .views import blog_create

app_name = 'blog'

urlpatterns = [
    path('blog-create', blog_create, name='create-blog'),
    # path('blog-detail', blog_detail, name='detail-blog'),
]