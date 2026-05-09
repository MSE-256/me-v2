from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meTime.urls')),  # 👈 esto incluye las URLs de tu app
]
