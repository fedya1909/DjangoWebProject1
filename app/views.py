"""
Definition of views.
"""
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import AnketaForm
from .forms import BlogForm

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Как с нами связаться',
            'year':datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

def videopost(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/videopost.html')

def blog(request):
	assert isinstance(request, HttpRequest)
	posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
	return render(
		request,
		'app/blog.html',
		{
			'title':'Блог',
			'posts': posts, # передача списка статей в шаблон веб-страницы
			'year':datetime.now().year,
		})

def blogpost(request, parametr):
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного 
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный 
            comment_f.save() # сохраняем изменения после добавления

            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки 
    else:
        form = CommentForm() # создание формы для ввода комментария
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,# передача конкретной статьи в шаблон веб-страницы
            'comments': comments,# передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form,# передача формы добавления комментария в шаблон веб-
            'year':datetime.now().year,
        })

def newpost(request):
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
            
            return redirect('blog')
    else:
        blogform = BlogForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',

            'year':datetime.now().year,
        })

def pool(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1':'Мужчина', '2':'Женщина'}
    ask_shoes = {'1':'Adidas','2':'Nike','3':'Puma','4':'Reebok','5':'New Balance'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data['gender']]
            data['ask_shoes'] = ask_shoes[form.cleaned_data['ask_shoes']]
            if(form.cleaned_data['interesting'] == True):
                data['interesting'] = 'Да'
            else:
                data['interesting'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/pool.html',
        {
            'form': form,
            'data': data,
        }
    )


def registration(request):
    
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('/')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html', {
            'regform': regform,
            'year': datetime.now().year,
        })

def links(request):
    return render(request, 'app/links.html', {'title': 'Ресурсы'})