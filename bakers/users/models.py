from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
            return f"{self.id}"
    class Meta:
        db_table='users'