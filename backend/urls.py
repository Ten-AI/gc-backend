# -*- coding: utf-8 -*-

"""
@author: hsowan <hsowan.me@gmail.com>
@date: 2019/12/4

"""

from django.urls import path

from . import apis

urlpatterns = [
    path('img/', apis.image_classify)
]
