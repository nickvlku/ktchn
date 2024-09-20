from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from households.views import HouseholdViewSet
from products.views import ProductViewSet, ProductTypeViewSet
from inventory.views import InventoryItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'households', HouseholdViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'inventory-items', InventoryItemViewSet)


urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]