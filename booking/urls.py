from django.urls import path
from .views import RestaurantsCreateAPIView, RestaurantsListAPIView, RestaurantsRetrieveAPIView, RestaurantsDetailView, HotelsDetailView, HotelsCreateAPIView, HotelsListAPIView, HotelsRetrieveAPIView, PlanViajeUpdateAPIView, PlanViajeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('plans-viewset', PlanViajeViewSet, basename='plan')

urlpatterns = [
    path('newrestaurant/', RestaurantsCreateAPIView.as_view(), name='restaurants-post'),
    path('restaurants/', RestaurantsListAPIView.as_view(), name='restaurants-list'),
    path('restaurant/', RestaurantsRetrieveAPIView.as_view(), name='restaurant'),
    path('editrestaurant/', RestaurantsDetailView.as_view(), name='edit-restaurant'),
    path('newhotel/', HotelsCreateAPIView.as_view(), name='hotel-post'),
    path('hotels/', HotelsListAPIView.as_view(), name='hotels-list'),
    path('hotel/', HotelsRetrieveAPIView.as_view(), name='hotel'),
    path('edithotel/', HotelsDetailView.as_view(), name='edit-hotel'),
    path('planviaje/', PlanViajeUpdateAPIView.as_view(), name='plan-viaje'),

]   