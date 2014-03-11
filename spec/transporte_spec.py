import unittest
from should_dsl import should
from transporte import Transporte

class Transporte_spec(unittest.TestCase):

    def it_creates_um_object_transporte(self):
        transporte = Transporte ('001','1001','www.1001.com.br','27338980','Rio','Bahia','R$ 3000')
        transporte.codTransporte |should| equal_to ('001')
        transporte.cia |should| equal_to ('1001')
        transporte.site |should| equal_to ('www.1001.com.br')
        transporte.telefone |should| equal_to ('27338980')
        transporte.origem |should| equal_to ('Rio')
        transporte.destino |should| equal_to ('Bahia')
        transporte.precoViagem |should| equal_to ('R$ 3000')

    def it_update(self):
    	transporte = Transporte ('001','1001','www.1001.com.br','27338980','Rio','Bahia','R$ 3000')
    	transporte.update('Itapemirim', 'www.Itapemirim.com.br', 'R$ 2200')
    	transporte.cia |should| equal_to('Itapemirim')
    	transporte.site |should| equal_to('www.Itapemirim.com.br')
    	transporte.precoViagem |should| equal_to('R$ 2200')    
