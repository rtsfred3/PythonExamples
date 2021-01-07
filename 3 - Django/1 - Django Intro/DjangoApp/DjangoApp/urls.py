from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('first_app/', include('apps.first_app.urls')),
    path('blog_app/', include('apps.blog_app.urls')),
    path('admin/', admin.site.urls),
]
