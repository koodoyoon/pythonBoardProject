"""
파일명 : forms.py
설명 :
생성일 : 2023/02/08
생성자 : koodoyoon

since 2023-01-09
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")


class Meta:
    model = User
    # password1 , password2 (비밀번호1을 제대로 입력했는지 대조하기 위한 값)
    fields = ('username', 'password1', 'password2', "email")
