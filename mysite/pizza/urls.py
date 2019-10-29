from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('pizza/', include('pizza.urls')),
    path('admin/', admin.site.urls),
]
