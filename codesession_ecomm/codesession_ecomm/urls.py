from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, URLPattern
from codesession_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("codesession_app.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
