from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from mainapp.views import ProductViewSet, ProductCartViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView



router = SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-cart', ProductCartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_schema', get_schema_view(title='E-Commerce', description='API description'), name='schema_url'),
    path('swagger_ui', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url': 'api_schema'}), name='swagger_ui')

]
