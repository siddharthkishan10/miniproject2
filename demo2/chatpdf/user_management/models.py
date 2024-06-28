from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_lecturer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)  # For lecturer approval

    def __str__(self):
        return self.username
