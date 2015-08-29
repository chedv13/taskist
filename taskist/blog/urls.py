from django.conf.urls import url
from taskist.blog import views

urlpatterns = [
    url(
        regex=r'^posts/$',
        view=views.PostListView.as_view(),
        name='list'
    )
]
