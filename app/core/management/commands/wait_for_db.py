"""
Comando Django para aguardar a inicialização do banco de dados.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Comando Django para aguardar o banco de dados"""

    def handle(self, *args, **options):
        pass