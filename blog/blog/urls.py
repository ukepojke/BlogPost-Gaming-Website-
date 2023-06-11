from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('post/<int:id>',include('main.urls')),
    path('category/',include('main.urls')),
    path('category/<int:id>',include('main.urls')),
    path('post/create/',include('main.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
