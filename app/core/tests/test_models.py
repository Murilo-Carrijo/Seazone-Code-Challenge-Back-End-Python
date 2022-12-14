"""
Testes para as models.
"""
from decimal import Decimal

from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Teste das MOodels"""

    def test_create_properties(self):
        """Teste para adicionar um novo imóvel com sucesso"""

        properties = models.Properties.objects.create(
            title='Imóvel 1',
            max_people=10,
            qty_bathrooms=2,
            pet_frendly=True,
            cleaning_value=Decimal('50.50'),
        )

        self.assertEqual(str(properties), properties.title)

    def test_create_advertisement(self):
        """Teste para adicionar um novo anuncio com sucesso"""

        properties = models.Properties.objects.create(
            title='Imóvel 1',
            max_people=10,
            qty_bathrooms=2,
            pet_frendly=True,
            cleaning_value=Decimal('50.50'),
        )

        advertisement = models.Advertisement.objects.create(
            title='Aluga-se',
            property_id=properties,
            ad_platform='AirBnb',
            plataform_fee=Decimal('4.99'),
        )

        self.assertEqual(
            str(advertisement),
            f'({advertisement.title} - {advertisement.ad_platform})',
        )
