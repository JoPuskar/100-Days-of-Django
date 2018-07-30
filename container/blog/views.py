
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Blog
from .forms import BlogForm


def blog_create(request):
    template_name = "blog/create_blog.html"

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            photo = form.cleaned_data['photo']
            new_blog = Blog.objects.create(title=title, body=body, photo=photo)
            new_blog.save()
            return redirect(reverse('blog:detail-blog', kwargs={'pk': new_blog.id}))
    else:
        form = BlogForm()
    return render(request, template_name, {'form': form})


def blog_detail(request, pk):
    template_name = "blog/blog_detail.html"

    blog = get_object_or_404(Blog, pk=pk)

    context = {
        'title': blog.title,
        'body': blog.body,
        'photo': blog.photo,
        'created_at': blog.created_at,
        'last_updated': blog.last_updated,
    }

    return render(request, template_name, context)
