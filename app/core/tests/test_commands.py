"""
Teste dos comandos de gerenciamento do Django
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Testando commandos"""

    def test_wait_for_db_ready(self, patched_check):
        """Testando se o banco de dados esta pronto"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databese=['default'])
    
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Testando quando OperationalError é capturado esperando pelo banco de dados"""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 +[True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_cout, 6)
        patched_check.assert_called_with(database=['default'])

