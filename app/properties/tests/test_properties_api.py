"""
Testes para as APIs referente aos Imóveis
"""

from decimal import Decimal
import json

from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from core.models import Properties

from properties.serializers import PropertiesSerializer, PropertyDetailSerializer

PROPERTIES_URL = reverse('properties:properties-list')


def detail_url(property_id):
    """Criar e retornar os detalhes da URL"""
    return reverse('properties:properties-detail', args=[property_id])

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

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

class PropetiesAPITest(TestCase):
    """Teste dos requests da API"""

    def test_retrive_properties(self):
        """Testando a requisição da lista de imóveis."""
        create_properties()
        create_properties()

        res = self.client.get(PROPERTIES_URL)

        properties_list = Properties.objects.all().order_by('-id')
        serializer = PropertiesSerializer(properties_list, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_property_detail(self):
        """Teste de retornar os detalhes do imóvel."""
        new_property = create_properties()

        url = detail_url(new_property.id)
        res = self.client.get(url)

        serializer = PropertyDetailSerializer(new_property)
        self.assertEqual(res.data, serializer.data)

    def teste_create_property(self):
        """Teste para adicionar um novo imóvel."""
        payload = {
            'title': 'Imóvel 1',
            'max_people': 5,
            'qty_bathrooms': 2,
            'pet_frendly': True,
            'cleaning_value': Decimal('50.50'), 
        }

        res = self.client.post(PROPERTIES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        new_property = Properties.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(new_property, k), v)
    
    def test_partial_update(self):
        """Teste para a edição parcial do imóvel."""
        new_property = create_properties()
        new_title = {'title': 'Imóvel 1 atualizado'}
        payload = json.dumps(new_title)
        url = detail_url(new_property.id)
        res = self.client.patch(url, payload, content_type='application/json')


        self.assertEqual(res.status_code, status.HTTP_200_OK)
        new_property.refresh_from_db()
        self.assertEqual(new_property.title, new_title['title'])
        self.assertEqual(new_property.max_people, 5)

    def test_full_update(self):
        """Teste para a edição total do imóvel."""
        new_property = create_properties()
        edit_property = {
            'title': 'Imóvel 1 atualizado',
            'max_people': 7,
            'qty_bathrooms': 3,
            'pet_frendly': False,
            'cleaning_value': '75.99', 
        }
        payload = json.dumps(edit_property)
        url = detail_url(new_property.id)
        res = self.client.put(url, payload, content_type='application/json')


        self.assertEqual(res.status_code, status.HTTP_200_OK)
        new_property.refresh_from_db()
        self.assertEqual(new_property.title, edit_property['title'])
        self.assertEqual(new_property.max_people, edit_property['max_people'])
        self.assertEqual(new_property.qty_bathrooms, edit_property['qty_bathrooms'])
        self.assertEqual(new_property.pet_frendly, edit_property['pet_frendly'])

    def test_delete_property(self):
        """Teste para deletar imóvel"""
        new_property = create_properties()
        url = detail_url(new_property.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Properties.objects.filter(id=new_property.id).exists())






        