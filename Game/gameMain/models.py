from django.db import models

# Create your models here.

class createNewRoom(models.Model):
    def __str__(self) -> str:
        return f"{self.id}"