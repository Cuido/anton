from django.db import models
from django.core.validators import MinLengthValidator
from cuido.enums.gender import Gender


GENDER_TYPES = [
    (Gender.MALE.value, Gender.MALE.name),
    (Gender.FEMALE.value, Gender.FEMALE.name),
    (Gender.OTHERS.value, Gender.OTHERS.name)
]


class User(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    phone_number = models.CharField(null=False, blank=False, max_length=10, validators=[MinLengthValidator(10)])
    email_id = models.EmailField(null=False, blank=False)
    gender = models.SmallIntegerField(choices=GENDER_TYPES, null=False, blank=False)
    persona = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'cuido'
        db_table = 'user'
