from django.db import models

# Create your models here.
class Index(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(max_length=13, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} \n{self.last_name} \n{self.phone_number}"