from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import BlogPost, BlogImage, BlogComments
from .forms import CommentForm


def blog_feed(request):
    #order by newest first for blog_post
    blog_post = BlogPost.objects.all().order_by('-created_on')
    blog_image = BlogImage.objects.all()
    total_post_number = blog_post.count()

    category_dict = dict()
    for key in blog_post:
        if key.category in category_dict.keys():
            category_dict[key.category] += 1
        else:
            category_dict[key.category] = 1

    # Pagination
    paginator = Paginator(blog_post, 5)
    page = request.GET.get('page')

    try:
        blog_post = paginator.page(page)
    except PageNotAnInteger:
        blog_post = paginator.page(1)
    except EmptyPage:
        blog_post = paginator.page(paginator.num_pages)

    context = {
        'blog_post': blog_post,
        'blog_image': blog_image,
        'category_dict': category_dict,
        'total_post_number': total_post_number,
    }

    return render(request, 'blog/blog.html', context)


def category_view(request, category):
    blog_post = BlogPost.objects.all().order_by('-created_on')
    selected_blog = blog_post.filter(category__icontains=category)
    total_post_number = blog_post.count()
    blog_image = BlogImage.objects.all()
    blog_post = BlogPost.objects.all()

    category_dict = dict()
    for key in blog_post:
        if key.category in category_dict.keys():
            category_dict[key.category] += 1
        else:
            category_dict[key.category] = 1

    context = {
        'selected_blog': selected_blog,
        'blog_image': blog_image,
        'category_dict': category_dict,
        'category': category,
        'total_post_number': total_post_number,
    }

    return render(request, 'blog/post_category_view.html', context)


def post_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_image = BlogImage.objects.get(article_id=blog_post.id)
    new_comment = None
    template = 'blog/post_detail.html'

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article_id = blog_post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'blog_image': blog_image,
        'comment_form': comment_form,
    }

    return render(request, template, context)
