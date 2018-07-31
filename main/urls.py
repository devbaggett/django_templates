from django.contrib import admin
from django.conf.urls import url, include
from apps.basic_app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^basic_app/', include('apps.basic_app.urls')),
]
