from django.contrib.auth.hashers import make_password
from django.db import models
from abstaction.created import BaseModel

USER_ROLES = (
    (1, 'Teacher'),
    (2, 'Student'),
    (3, 'Admin'),
)

class User(BaseModel):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    role = models.IntegerField(default=2,choices=USER_ROLES)

    @property
    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



