from django.shortcuts import get_object_or_404, render
from posts_app.models import Posts
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from posts_app.forms import PostsForm

# Create your views here.
def post_list(request):
    template_name = 'post-list.html'
    posts = Posts.objects.all()
    context = {
        'posts':posts
        }
    return render(request, template_name, context)

def post_detail(request, id):
    template_name = 'post-detail.html'
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, template_name, context)

def post_create(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            messages.success(request, 'O post foi criado com sucesso')
            return HttpResponseRedirect(reverse('post-list'))

    form = PostsForm()
    return render(request, 'post-form.html', {"form": form})

def post_detail(request, id):
    template_name = 'post-detail.html'
    post = Posts.objects.get(id=id)
    print(post)
    context = {
        'post': post
    }
    return render(request, template_name, context)
    
def post_update(request, id):
    post = get_object_or_404(Posts, id=id)
    form = PostsForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
            form.save()

            messages.success(request, 'post atualizado')
            return HttpResponseRedirect(reverse('post-detail', args=[post.id]))
    return render(request, 'post-form.html', {"form":form})

def post_delete(request, id):
    post=Posts.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'post deletado com sucesso')
        return HttpResponseRedirect(reverse('post-list'))
    return render(request, 'post-delete.html')

