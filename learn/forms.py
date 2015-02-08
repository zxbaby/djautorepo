#coding:utf8

from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
