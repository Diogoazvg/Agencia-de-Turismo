import unittest
from should_dsl import should
from refeicao import Refeicao

class Refeicao_spec(unittest.TestCase):

    def it_criar_um_objeto_refeicao(self):
        refeicao = Refeicao('001','Le coco','www.lecoco.com.br','1127378977','5','R$ 67')
        refeicao.codRefeicao |should| equal_to ('001')
        refeicao.restaurante |should| equal_to ('Le coco')
        refeicao.site |should| equal_to ('www.lecoco.com.br')
        refeicao.telefone |should| equal_to ('1127378977')
        refeicao.quantRefeicao |should| equal_to ('5')
        refeicao.precoKg |should| equal_to ('R$ 67')

