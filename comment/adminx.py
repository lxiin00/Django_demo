from django.contrib import admin
from .models import Commnet
from django_demo1.custom_site import custom_site

import xadmin


# @admin.register(Commnet, site=custom_site)
class CommentAdmin(object):
    model_icon = 'fa fa-comments'
    # list_display = (
    #     'target', 'nickname', 'content', 'website', 'created_time'
    # )
    list_display = (
        'target', 'nickname', 'content', 'created_time'
    )

xadmin.site.register(Commnet, CommentAdmin)