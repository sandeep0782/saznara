from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



# Create your models here.
USER_ROLE = (
    ('None', 'None'),
    ('Admin', 'Admin'),
    ('Buyer', 'Buyer'),
    ('Supplier', 'Supplier')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role  = models.CharField(max_length=50, choices=USER_ROLE, default='None')
    company = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.CharField(max_length=12, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    pin = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{6}$', 'Enter a valid 6-digit PIN code')], null=True, blank=True )
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'