from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            return HttpResponseRedirect('/blog-create')
    else:
        form = BlogForm()
    return render(request, template_name, {'form': form})