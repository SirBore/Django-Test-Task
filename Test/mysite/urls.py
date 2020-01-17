from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from mysite.books import views

urlpatterns = [
	 url(r'^admin/', admin.site.urls),
	url('accounts/', include('django.contrib.auth.urls')),
	url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]
