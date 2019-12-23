from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogType, Blog
from markdown import markdown

# Create your views here.
def blog_list(request):
    context = {}
    blogs_all = Blog.objects.all()
    context['num_all'] = blogs_all.count()

    blogs = blogs_all
    paginator = Paginator(blogs, 10)  # 每十页分一页
    page_index = request.GET.get('page', 1)
    context['page'] = paginator.get_page(page_index)


    context['active_all'] = 1
    context['types'] = []
    for blog_type in BlogType.objects.all():
        context['types'].append({
                'blog_type': blog_type,
                'num': Blog.objects.filter(blog_type=blog_type).count(),
                'active': 0,
        })
    return render(request, 'blog/blog_list.html', context)


def blog_list_with_type(request, blog_type_pk):
    context = {}
    blogs_all = Blog.objects.all()
    context['num_all'] = blogs_all.count()

    context['type'] = get_object_or_404(BlogType, pk=blog_type_pk)  #########
    blogs = Blog.objects.filter(blog_type=context['type'])  #########
    paginator = Paginator(blogs, 10)  # 每十页分一页
    page_index = request.GET.get('page', 1)
    context['page'] = paginator.get_page(page_index)


    context['active_all'] = 0  #########
    context['types'] = []
    for blog_type in BlogType.objects.all():
        context['types'].append({
            'blog_type': blog_type,
            'num': Blog.objects.filter(blog_type=blog_type).count(),
            'active': blog_type.pk == blog_type_pk,
        })

    return render(request, 'blog/blog_list_with_type.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    context['blog'].content = markdown(context['blog'].content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'blog/blog_detail.html', context)
