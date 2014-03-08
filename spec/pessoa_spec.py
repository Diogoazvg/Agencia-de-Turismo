import unittest
from should_dsl import should
from pessoa import Pessoa

class Pessoa_spec(unittest.TestCase):

    def it_creates_a_pessoa_object(self):
        pessoa = Pessoa ('001','Diogo','3','998845108','diogo.azvg@gmail.com')
        pessoa.codPessoa |should| equal_to ('001')
        pessoa.cliente |should| equal_to ('Diogo')
        pessoa.quantDependente |should| equal_to ('3')
        pessoa.telefone |should| equal_to ('998845108')
        pessoa.email |should| equal_to ('diogo.azvg@gmail.com')

