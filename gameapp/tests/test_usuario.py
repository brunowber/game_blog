# -*- coding: utf-8 -*-
import unittest


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        from gameapp.forms import UsuarioForm

        usuario1 = {'username': 'brunoweber', 'password': 'bruno1234',
                    'first_name': 'Bruno', 'last_name': 'Weber',
                    'jogo': 'Uncharted'}
        self.form1 = UsuarioForm(data=usuario1)

        usuario2 = {'username': '', 'password': 'bruno1234',
                    'first_name': 'Bruno', 'last_name': 'Weber',
                    'jogo': 'Uncharted'}
        self.form2 = UsuarioForm(data=usuario2)

        usuario3 = {'username': 'brunoweber', 'password': '',
                    'first_name': 'Bruno', 'last_name': 'Weber',
                    'jogo': 'Uncharted'}
        self.form3 = UsuarioForm(data=usuario3)

        usuario4 = {'username': 'brunoweber', 'password': 'bruno1234',
                    'first_name': 'Bruno', 'last_name': 'Weber',
                    'jogo': ''}
        self.form4 = UsuarioForm(data=usuario4)

    def test(self):
        self.assertEquals(self.form1.is_valid(), True)  # Todos os dados
        self.assertEquals(self.form2.is_valid(), False)  # Sem usuário
        self.assertEquals(self.form3.is_valid(), False)  # Sem senha
        self.assertEquals(self.form4.is_valid(), False)  # Sem jogo
