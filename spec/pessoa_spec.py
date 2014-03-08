import unittest
from should_dsl import should
from pessoa import Pessoa

class Pessoa_spec(unittest.TestCase):

    def it_creates_a_pessoa_object(self):
        pessoa = Pessoa ('001','Diogo','3','998845108','diogo.azvg@gmail.com')

