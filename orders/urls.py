from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, BulkOrderViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='orderitem')
router.register(r'bulk-orders', BulkOrderViewSet, basename='bulkorder')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = router.urls
