from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Post, Tag
from .adminforms import PostAdminForm
from django_demo1.custom_site import custom_site
# from django_demo1.adminx import BaseOwnerAdmin

from django.contrib.admin.models import LogEntry

from xadmin.layout import Row, Fieldset, Container
import xadmin
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter

from xadmin import views
from django.apps import AppConfig


class ThemeSettings(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, ThemeSettings)


class GlobalSettings(object):
    site_title = '博客后台管理'
    site_footer = '博客后台管理'
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSettings)


class PostInline:
    # fields = ['title', 'desc']
    form_layout = (
        Fieldset(
            # '文章信息',
            Row('title', 'desc'),
        )
    )
    extra = 1
    model = Post


# @xadmin.site.register(Category)
class CategoryAdmin(object):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    model_icon = 'fa fa-bell'
    # fields = ('name', 'status', 'is_nav')
    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            'name',
            'status',
            # 'is_nav',
        ),
        Fieldset(
            '其他设置',
            'is_nav'
        )
    )

    # inlines = [PostInline]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def queryset(self):
        request = self.request
        qs = super().queryset()
        return qs.filter(owner=request.user)


    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

xadmin.site.register(Category, CategoryAdmin)


# @xadmin.site.register(Tag)
class TagAdmin(object):
    list_display = ('name', 'status', 'created_time')
    # fields = ('name', 'status')
    model_icon = 'fa fa-tags'
    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            'name',
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


xadmin.site.register(Tag, TagAdmin)


class CategoryOwnerFilter(RelatedFieldListFilter):

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path,):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')

manager.register(CategoryOwnerFilter, take_priority=True)


# @xadmin.site.register(Post)
class PostAdmin(object):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time',
        'operator'
    ]
    model_icon = 'fa fa-edit'
    list_display_links = []
    list_filter = ['category']
    search_fields = ['title', 'category__name']

    actions_on_top = True
    # actions_on_bottom = True
    # save_on_top = True

    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'tag',
            'status',

        ),
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content'
        ),
    )


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=[obj.id])
        )
    operator.short_description = '操作'

    def queryset(self):
        request = self.request
        qs = super().queryset()
        return qs.filter(owner=request.user)


    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

xadmin.site.register(Post, PostAdmin)

# @xadmin.site.register(LogEntry)
# class LogEntryAdmin(object):
#     list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
#
# xadmin.site.register(LogEntry, LogEntryAdmin)