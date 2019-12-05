#!/usr/bin/env python
# coding: utf8
# author: channel
#
from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField

from cmdb import models

class UserInfoForm(forms.Form):
    user = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={'class':'c1'})
    )

    pwd = fields.CharField(
        max_length=12,
        widget=widgets.PasswordInput(attrs={'class':'c1'})
    )

    user_type = fields.CharField(
        # choices = [(0,'超级用户'),(1,'普通用户')]
        choices = [],
        widget=widgets.Select
    )


    user_type2 = fields.CharField(widget=widgets.Select(choices=[]))

    def __init__(self,*args, **kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)

        self.fields['user_type'].choices=models.UserType.objects.values_list('id','name')
        self.fields['user_type2'].widget.choices=models.UserType.objects.values_list('id','name')

