from django.db import models


class Rental(models.Model):
    name = models.CharField(
        unique=True, verbose_name="Rental name",
        max_length=100
    )


class Reservation(models.Model):
    checkin = models.DateField(verbose_name="Check-in date")
    checkout = models.DateField(verbose_name="Check-out date")
    rental_id = models.ForeignKey(
        Rental, on_delete=models.CASCADE, related_name="reservations"
    )

    class Meta:
        ordering = ["checkin", "checkout"]
