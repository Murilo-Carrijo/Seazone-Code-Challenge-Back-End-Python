from django.db import models
# from django.conf import settings


class Properties(models.Model):
    """Imóveis object."""
    title = models.CharField(max_length=255)
    max_people = models.IntegerField()
    qty_bathrooms = models.IntegerField()
    pet_frendly = models.BooleanField()
    cleaning_value = models.DecimalField(max_digits=5, decimal_places=2)
    activation_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
