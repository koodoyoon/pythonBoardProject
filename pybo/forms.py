"""
파일명 : forms.py
설명 : html form 관리
생성일 : 2023/02/01
생성자 : koodoyoon

since 2023-01-09
"""

from django import forms
from pybo.models import Question, Answer, Board


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  # 시용할 Answer model

        fields = ['content']  # AnswerForm 사용할 Answer model 속성

        labels = {
            'content': '답변내용'
        }


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board

        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 question

        fields = ['subject', 'content']  # QuestionForm에서 사용할 question model의 속성

        labels = {
            'subject': '제목',
            'content': '내용',
        }
