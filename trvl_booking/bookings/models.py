from django.db import models

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField()
    number_of_travelers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination