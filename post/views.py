from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostCreateForm
from uuslug import slugify


def blog(request):
    last_post = Post.objects.first()
    posts = Post.objects.exclude(id=last_post.id)
    return render(request, 'blog.html', {'posts': posts,
                                         'last_post': last_post})

def post(request, id, slug):
    post = Post.objects.get(id=id, slug=slug)
    return render(request, 'post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.slug = slugify(form.cleaned_data['title'])
            new.save()
            return redirect('post:blog')
    else:
        form = PostCreateForm
    return render(request, 'create_post.html', {'form': form})
    
def del(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post:blog')