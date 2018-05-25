from django.http import JsonResponse
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post


def api_v1_posts(request):

    # 絞り込み検索
    if request.method == 'GET':
        query = request.GET.get('query')
        title_list = [post.title for post in Post.objects.filter(title__icontains=query)]
        d = {
            'result_list': title_list
        }
        return JsonResponse(d)

    # 新規作成
    elif request.method == 'POST':
        title = request.POST.get('title')
        post = Post(title=title)
        post.save()
        d = {
            'pk': post.pk,
            'created_at': post.created_at,
            'title': post.title,
        }
        return JsonResponse(d)
