from django.db import models


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


class Advertisement(models.Model):
    """Anúncio object"""
    title = models.CharField(max_length=255)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    ad_platform = models.CharField(max_length=50)
    plataform_fee = models.DecimalField(max_digits=4, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'({self.title} - {self.ad_platform})'
