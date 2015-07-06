from django.conf.urls import patterns, url
from Datalib import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Data_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.index, name='index'),
    url(r'^insert/$', views.insert, name='insert'),
    url(r'^delete/(?P<person_id>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<person_id>\d+)$', views.edit, name='edit')
)
