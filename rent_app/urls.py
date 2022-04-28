from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RentViewSet, ReservationViewSet, RentTableView


router = DefaultRouter()
router.register("rent", RentViewSet, basename="rent")
router.register("reservation", ReservationViewSet, basename="reserv")


urlpatterns = [
    path("", include(router.urls)),
    path("table/", RentTableView.as_view())
]
