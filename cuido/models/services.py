from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .user import User, CLA


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        app_label = 'cuido'
        db_table = 'services'


class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'cuido'
        db_table = 'payments'


class Bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='booked_user', on_delete=models.CASCADE)
    cla_id = models.ForeignKey(CLA, related_name='cla', on_delete=models.CASCADE)
    slot = models.CharField(max_length=100)
    service_id = models.ForeignKey(Services, related_name='service', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'cuido'
        db_table = 'bookings'


class Transactions(models.Model):
    booking_id = models.ForeignKey(Bookings, related_name='booking', on_delete=models.CASCADE)
    slot_start_time = models.DateTimeField(null=False, blank=False)
    slot_end_time = models.DateTimeField(null=False, blank=False)
    payment_mode = models.ForeignKey(Payment, related_name='payment', on_delete=models.CASCADE)
    actual_payable = models.IntegerField(null=False, blank=False)
    amount_payable = models.IntegerField(null=False, blank=False)
    cuido_cash_used = models.IntegerField(null=True, blank=True)
    discount_availed = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'cuido'
        db_table = 'transactions'


class UserFeedback(models.Model):
    user_id = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Bookings, related_name='bookings', on_delete=models.CASCADE)
    service_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cla_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'cuido'
        db_table = 'user_feedback'
