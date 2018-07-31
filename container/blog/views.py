
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Blog
from .forms import BlogForm


def blog_create(request):
    template_name = "blog/create_blog.html"

    form = BlogForm(request.POST, request.FILES or None)
    if request.method == 'POST':
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
        'blog': blog,
    }

    return render(request, template_name, context)


def blog_edit(request, pk):
    template_name = "blog/create_blog.html"

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        edit_form = BlogForm(data=request.POST, files=request.FILES)

        print(edit_form.errors)
        if edit_form.is_valid():
            print("valid")
            title = edit_form.cleaned_data['title']
            body = edit_form.cleaned_data['body']
            photo = request.FILES['photo']
            Blog.objects.filter(id=pk).update(title=title, body=body, photo=photo)
            return redirect(reverse('blog:detail-blog', kwargs={'pk': blog.pk}))
    else:
        edit_form = BlogForm(initial={'title': blog.title, 'body': blog.body,
                                               'photo': blog.photo})

    context = {
        'form': edit_form
    }

    return render(request, template_name, context)


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "blog/blog_list.html", context={'blogs': blogs})