from django.conf.urls import url
from django.contrib import admin
from .views import PostList, api_v1_posts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^api/v1/posts$', api_v1_posts, name='api_v1_posts'),
]
