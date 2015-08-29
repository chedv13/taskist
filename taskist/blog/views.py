__author__ = 'chedv13'

from taskist.blog.models import Post
from taskist.blog.serializers import PostSerializer
from rest_framework import viewsets
from django.template import loader, Context
from django.http import HttpResponse
from django.views.generic import ListView


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(ListView):
    model = Post


def main_view(request):
    t = loader.get_template('views/main.html')
    c = Context({'posts': [1, 2, 3]})
    return HttpResponse(t.render(c))
