from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'felix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.receive_message, name='home'),
    url(r'^home1/', views.home1page, name='home1'),
    url(r'^thanks/', views.thanks_page, name='thanks'),
    url(r'^$', views.index, name='index'),
)
