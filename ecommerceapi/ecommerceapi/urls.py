from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from mainapp.views import ProductViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
