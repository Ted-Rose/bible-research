from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line will make your API endpoints available under /api/v1/
    path('api/v1/', include('bible.urls')),
    # This is useful for logging into the browsable API if you use DRF's authentication
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
