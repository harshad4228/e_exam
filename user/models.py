from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin1 = models.BooleanField(default=False,null=True)
    GENDER_CHOICES = [
        (False, 'Male'),
        (True, 'Female')
    ]
    gender = models.BooleanField(choices=GENDER_CHOICES,default=False)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    
    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        # Send welcome email to user
        if not self.pk:
            send_mail(
                'Welcome to our website!',
                'Dear {},\n\nThank you for registering on our website!'.format(self.username),
                'from@gmail.com',
                [self.email],
                fail_silently=False,
            )
        super(User, self).save(*args, **kwargs)
