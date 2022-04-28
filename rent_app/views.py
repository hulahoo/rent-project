from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .models import Rental, Reservation
from .serializers import RentSerializer, ReservationSerializer, RentTableSerializer


class RentViewSet(ModelViewSet):
    queryset = Rental.objects.all()
    model = Rental
    serializer_class = RentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["action"] = self.action
        return context


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    model = Reservation
    serializer_class = ReservationSerializer


class RentTableView(ListAPIView):
    model = Rental
    serializer_class = RentTableSerializer
    queryset = Rental.objects.all()
