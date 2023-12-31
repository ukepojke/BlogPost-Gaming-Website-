from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator


def home(re):
    posts = Post.objects.all()
    p = Paginator(posts,4)
    page = re.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    return render(re,'index.html',{'posts': posts,'venues': venues,'nums': nums})

def post_detail(re,id):
    post = Post.objects.get(id=id)
    category = Category.objects.all().order_by('category')
    if re.method == 'POST':
        form = CommentForm(data=re.POST)
        data = form.save(commit=False)
        data.post = post
        data.save()

    form = CommentForm()
    return render(re,'detail_view.html',{'post': post, 'category': category,'form':form})

def post_category(re):
    post_category = Category.objects.all()
    p = Paginator(post_category, 4)
    page = re.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    return render(re,'category.html',{'post_category': post_category, 'venues': venues,'nums': nums})

def detail_category(re,id):
    category_id = Category.objects.get(id=id)
    posts = Post.objects.filter(category=category_id)
    p = Paginator(posts, 2)
    page = re.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    return render(re,'detail_category.html',{'posts':posts,'category': category_id,'venues': venues,'nums': nums})

def post_create(re):
    form = PostForm()
    if re.method == 'POST':
        form = PostForm(data=re.POST,files=re.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return redirect('/')
    form = PostForm()
    return render(re,'post_create.html',{'form':form})


