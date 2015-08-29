__author__ = 'chedv13'

from taskist.blog.models import Post
from taskist.blog.serializers import PostSerializer
from rest_framework import viewsets
from django.views.generic import ListView, TemplateView
from taskist.blog.forms import PostForm


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(ListView):
    model = Post


class PostFormView(TemplateView):
    template_name = 'blog/post_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostFormView, self).get_context_data(**kwargs)
        context.update(post_form=PostForm())

        return context
