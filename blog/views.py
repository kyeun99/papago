from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog1, Blog2, Blog3, Comment1, Comment2, Comment3
from .forms import CommentForm, DommentForm, EommentForm
# Create your views here.


def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    blogs = Blog1.objects
    blog_list=Blog1.objects.all()
    paginator = Paginator(blog_list,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/blog.html', {'blogs': blogs, 'posts':posts})

def alog(request):
    alogs = Blog2.objects
    alog_list=Blog2.objects.all()
    paginator = Paginator(alog_list,6)
    page = request.GET.get('page')
    aosts = paginator.get_page(page)
    return render(request, 'blog/alog.html', {'alogs': alogs, 'aosts':aosts})

def clog(request):
    clogs = Blog3.objects
    clog_list=Blog3.objects.all()
    paginator = Paginator(clog_list,6)
    page = request.GET.get('page')
    costs = paginator.get_page(page)
    return render(request, 'blog/clog.html', {'clogs': clogs, 'costs':costs})

def blogdetail(request, blog_id):
    blog_detail = get_object_or_404(Blog1, pk=blog_id)
    comments=Comment1.objects.all()
    return render(request, 'blog/blogdetail.html', {'blog': blog_detail, 'comments': comments})

    
def alogdetail(request, alog_id):
    alog_detail = get_object_or_404(Blog2, pk=alog_id)
    comments=Comment2.objects.all()
    return render(request, 'blog/alogdetail.html', {'alog': alog_detail, 'comments': comments})


def clogdetail(request, clog_id):
    clog_detail = get_object_or_404(Blog3, pk=clog_id)
    comments=Comment3.objects.all()
    return render(request, 'blog/clogdetail.html', {'clog': clog_detail, 'comments': comments})

def blognew(request):
    return render(request, 'blog/blognew.html')

def alognew(request):
    return render(request, 'blog/alognew.html')

def clognew(request):
    return render(request, 'blog/clognew.html')

def blogcreate(request):
    blog = Blog1()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def alogcreate(request):
    alog = Blog2()
    alog.title = request.GET['title']
    alog.body = request.GET['body']
    alog.pub_date = timezone.datetime.now()
    alog.save()
    return redirect('/alog/' + str(alog.id))

def clogcreate(request):
    clog = Blog3()
    clog.title = request.GET['title']
    clog.body = request.GET['body']
    clog.pub_date = timezone.datetime.now()
    clog.save()
    return redirect('/clog/' + str(clog.id))

def blogcomment_new(request, blog_id):
    post = get_object_or_404(Blog1, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment1 = form.save(commit= False)
            comment1.post = post
            comment1.save()
            return redirect('/blog/' + str(blog_id))
    else:
        form = CommentForm()
    return render(request, 'blog/blogcomment_new.html', {'form': form})

def alogcomment_new(request, alog_id):
    post = get_object_or_404(Blog2, pk=alog_id)
    if request.method == "POST":
        form = DommentForm(request.POST)
        if form.is_valid():
            comment2 = form.save(commit= False)
            comment2.post = post
            comment2.save()
            return redirect('/alog/' + str(alog_id))
    else:
        form = DommentForm()
    return render(request, 'blog/alogcomment_new.html', {'form': form})

def clogcomment_new(request, clog_id):
    post = get_object_or_404(Blog3, pk=clog_id)
    if request.method == "POST":
        form = EommentForm(request.POST)
        if form.is_valid():
            comment3 = form.save(commit= False)
            comment3.post = post
            comment3.save()
            return redirect('/clog/' + str(clog_id))
    else:
        form = EommentForm()
    return render(request, 'blog/clogcomment_new.html', {'form': form})

