"""
파일명 : pybo_filter.py
설명 :
생성일 : 2023/02/07
생성자 : koodoyoon

since 2023-01-09
"""

from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

