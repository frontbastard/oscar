from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    # Django admin site.
    path("admin/", admin.site.urls),
    # Oscar URLs.
    path("", include(apps.get_app_config("oscar").urls[0])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
