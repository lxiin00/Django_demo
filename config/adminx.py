from django.contrib import admin
from .models import Link, SideBar

from django_demo1.custom_site import custom_site
# from django_demo1.adminx import BaseOwnerAdmin

import xadmin
from xadmin.layout import Row, Fieldset, Container

# @xadmin.site.register(Link)
class LinkAdmin(object):
    list_display = (
        'title', 'href', 'status', 'weight', 'created_time'
    )
    model_icon = 'fa fa-cogs'

    # fields = (
    #     'title', 'href', 'status', 'weight'
    # )

    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            'title',
            'href',
            'weight',
            'status',
        )
    )

    def queryset(self):
        request = self.request
        qs = super().queryset()
        return qs.filter(owner=request.user)


    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

xadmin.site.register(Link, LinkAdmin)

# @xadmin.site.register(SideBar)
class SideBarAdmin(object):
    list_display = (
        'title', 'display_type', 'content', 'status', 'created_time'
    )
    model_icon = 'fa fa-code'

    def queryset(self):
        request = self.request
        qs = super().queryset()
        return qs.filter(owner=request.user)


    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

xadmin.site.register(SideBar, SideBarAdmin)
