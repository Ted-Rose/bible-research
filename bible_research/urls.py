from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('bible.urls')),
    path('api/v1/', include('annotations.urls')),
    # This is useful for logging into the browsable API if you use DRF's authentication
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
