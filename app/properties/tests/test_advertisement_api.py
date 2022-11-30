"""
Testes para a API de anúncios.
"""
from decimal import Decimal
import json

from django.urls import reverse
from django.test import TestCase

from rest_framework import status

from core.models import (
    Properties,
    Advertisement,
)

from properties.serializers import AdvertisementSerializer


ADVERTISEMENT_URL = reverse('properties:advertisement-list')


def detail_url(advertisement_id):
    """Criar e retornar os detalhes da URL"""
    return reverse('properties:advertisement-detail', args=[advertisement_id])


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
        'title': 'Casa de campo',
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
    
    def test_partial_update(self):
        """Teste para a edição parcial do anúncio"""
        new_advertisement = create_advertisement()
        new_title = {'title': 'Casa na praia'}
        payload = json.dumps(new_title)
        url = detail_url(new_advertisement.id)
        res = self.client.patch(url, payload, content_type='application/json')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        new_advertisement.refresh_from_db()
        self.assertEqual(new_advertisement.title, new_title['title'])
        self.assertEqual(new_advertisement.ad_platform, 'AirBnb')
    
    def test_full_update(self):
        """Teste para a edição total do anúncio."""
        new_advertisement = create_advertisement()
        print(new_advertisement.property_id.id)
        edit_advertisement = {
            'title': 'Casa na praia',
            'property_id': new_advertisement.property_id.id,
            'ad_platform': 'Trivago',
            'plataform_fee': '3.89',
        }

        payload = json.dumps(edit_advertisement)
        url = detail_url(new_advertisement.id)
        res = self.client.put(url, payload, content_type='application/json')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        new_advertisement.refresh_from_db()
        self.assertEqual(new_advertisement.title, edit_advertisement['title'])
        self.assertEqual(new_advertisement.property_id.id, edit_advertisement['property_id'])
        self.assertEqual(
            new_advertisement.ad_platform, edit_advertisement['ad_platform']
        )

    def test_delete_property(self):
        """Teste para deletar imóvel"""
        new_advertisement = create_advertisement()
        url = detail_url(new_advertisement.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Properties.objects.filter(id=new_advertisement.id).exists()
        )
