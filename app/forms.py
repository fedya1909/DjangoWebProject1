"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2,max_length=100)
    job = forms.CharField(label='Ваша работа', min_length=2,max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',choices=[('1','Мужской'),('2','Женский')],
                               widget=forms.RadioSelect, initial=1)
    ask_shoes = forms.ChoiceField(label='Ваша любимая фирма из предложенных',
                                  choices=(('1','Adidas'),
                                           ('2','Nike'),
                                           ('3','Puma'),
                                           ('4','Reebok'),
                                           ('5','New Balance')),initial=1)
    interesting = forms.BooleanField(label='Вам интересен наш магазин?',
                                     required=False)
    email = forms.EmailField(label='Ваш e-mail',min_length=5)
    message = forms.CharField(label='Коротко о себе',
                              widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}