from rest_framework import serializers
from .models import Rental, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation["previous_reservation"] = instance.get_previous_by_checkout().id
        except Reservation.DoesNotExist:
            representation["previous_reservation"] = 0
        return representation


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        action = self.context.get("action")
        if action == "retrieve":
            representation['reservations'] = ReservationSerializer(
                instance.reservations.all(), many=True
            ).data
        return representation


class RentTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["reservations"] = ReservationSerializer(
                instance.reservations.all(), many=True
            ).data
        return representation
