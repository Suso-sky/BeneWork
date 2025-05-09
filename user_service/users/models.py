from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Almacenará el hash

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  # Evita hashear múltiples veces
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)