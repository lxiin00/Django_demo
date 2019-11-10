from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .custom_site import custom_site
# from blog.views import post_detail, post_list
from config.views import links

from blog.views import PostDetailView, IndexView, CategoryView, TagView, SearchView, AuthorView, LinkView
from comment.views import CommentView

from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

from django.conf import settings
from django.conf.urls import url, include, re_path
from django.conf.urls.static import static as static1
from .settings import base
from django.views import static

# from .autocomplete import CategoryAutocomplete, TagAutocomplete

from rest_framework.routers import DefaultRouter
from blog.api import PostViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls

import xadmin
import debug_toolbar

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    # url(r'^post/(?P<pk>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', LinkView.as_view(), name='links'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)$', AuthorView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    # url(r'^admin/', custom_site.urls, name='admin'),
    url(r'^admin/', xadmin.site.urls, name='xadmin'),
    # path(r'admin/', xadmin.site.urls, name='xadmin'),
    # url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    # url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    # url(r'^api/post/', PostList.as_view(), name='post-list'),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include_docs_urls(title='django_demo1 apis')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # re_path(r'^static/(?P<path>.*)', static.serve, {'document_root': base.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': base.MEDIA_ROOT}, name='media'),

]

# urlpatterns += static1(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns