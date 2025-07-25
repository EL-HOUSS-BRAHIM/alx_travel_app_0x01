from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, ReviewViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'reviews', ReviewViewSet, basename='review')

# The urlpatterns list routes URLs to views
urlpatterns = [
    # path('', include(router.urls)),  # Include all the routes from the router
    path('api/', include(router.urls)),

]