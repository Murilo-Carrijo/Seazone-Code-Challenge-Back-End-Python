"""
Testes para a API de anúncios.
"""
from decimal import Decimal

from django.urls import reverse
from django.test import TestCase

from rest_framework import status

from core.models import (
    Properties,
    Advertisement,
)

from properties.serializers import AdvertisementSerializer


ADVERTISEMENT_URL = reverse('properties:advertisement-list')


def create_properties(**params):
    """Criar e retornar o imóvel"""
    defaults = {
        'title': 'Imóvel 1',
        'max_people': 5,
        'qty_bathrooms': 2,
        'pet_frendly': True,
        'cleaning_value': Decimal('50.50'),
    }
    defaults.update(params)

    new_property = Properties.objects.create(**defaults)
    return new_property

def create_advertisement(**params):
    """Criar e retornar o anúncio"""
    properties = create_properties()

    defaults = {
        'property_id': properties,
        'ad_platform': 'AirBnb',
        'plataform_fee': Decimal('4.99'),
    }

    defaults.update(params)

    advertisement = Advertisement.objects.create(**defaults)
    return advertisement


class AdvertisementAPITest(TestCase):
    """Teste dos requests da API"""
    def test_retrieve_advertisement(self):
        """Testando a requisição da lista de anúncios."""
        create_advertisement()
        create_advertisement()

        res = self.client.get(ADVERTISEMENT_URL)

        all_advertisement = Advertisement.objects.all().order_by('-id')
        serializer = AdvertisementSerializer(all_advertisement, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
