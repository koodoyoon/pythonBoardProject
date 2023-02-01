"""
파일명 : forms.py
설명 : html form 관리
생성일 : 2023/02/01
생성자 : koodoyoon

since 2023-01-09
"""

from django import forms
from pybo.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 question

        fields = ['subject', 'content']  # QuestionForm에서 사용할 question model의 속성
        widgets = {  # 속성 추가 : class rows 추가
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }
