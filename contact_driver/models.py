from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    license_plate_number = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    contact_method = models.CharField(max_length=10, choices=[('call', 'Call'), ('email', 'Email'), ('sms', 'SMS')])
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.username
