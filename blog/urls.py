from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    url(r'^blogger/(?P<pk>\d+)$', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    url(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    url(r'^blog/(?P<pk>\d+)/comment/$', views.BlogCommentCreate.as_view(), name='blog_comment'),
]