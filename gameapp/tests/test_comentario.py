# -*- coding: utf-8 -*-
import unittest


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        from gameapp.forms import ComentarioForm

        comentario1 = {'comentario': 'olaaaaaa'}
        self.form1 = ComentarioForm(data=comentario1)

        comentario2 = {'comentario': ''}
        self.form2 = ComentarioForm(data=comentario2)

        comentario3 = {}
        self.form3 = ComentarioForm(data=comentario3)

    def test(self):
        self.assertEquals(self.form1.is_valid(), True)  # Todos os dados
        self.assertEquals(self.form2.is_valid(), False)  # Comentario Vazio
        self.assertEquals(self.form3.is_valid(), False)  # Sem dados

