# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from taskist.blog import views as blog_views
from taskist.users import views as users_views

router = DefaultRouter()
router.register(r'posts', blog_views.PostViewSet)
router.register(r'users', users_views.UserViewSet)

# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
]

urlpatterns += [url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
                url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
                url(r'^admin/', include(admin.site.urls)),
                url(r'^users/', include("taskist.users.urls", namespace="users")),
                url(r'^blog/', include("taskist.blog.urls", namespace="posts")),
                url(r'^accounts/', include('allauth.urls'))] + static(settings.MEDIA_URL,
                                                                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error')
    ]
