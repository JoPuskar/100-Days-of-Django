from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('blog-create', views.blog_create, name='create-blog'),
    path('blog-detail/<int:pk>', views.blog_detail, name='detail-blog'),
    path('blog-edit/<int:pk>', views.blog_edit, name='edit-blog'),
    path('blog-list/', views.blog_list, name='blog-list'),
]