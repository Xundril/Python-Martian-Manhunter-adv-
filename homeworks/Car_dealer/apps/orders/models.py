from django.core.validators import RegexValidator
from django.db import models


class Order(models.Model):
    STATUS_OPEN = 'open'
    STATUS_IN_PROGRESS = 'in progress'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = (
        (STATUS_OPEN, "Open"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled")
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
    )
    first_name = models.CharField(
        max_length=80,
    )
    last_name = models.CharField(
        max_length=80,
    )
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(
        validators=[phoneNumberRegex],
        max_length=16,
    )
    message = models.TextField(
        blank=True,
    )

    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
        related_name='orders',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
