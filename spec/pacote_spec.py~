import unittest
from should_dsl import should
from pacote import Pacote
from pessoa import Pessoa
from transporte import Transporte
from hotel import Hotel
from refeicao import Refeicao

class Pacote_spec(unittest.TestCase):

    def it_criar_um_objeto_pacote(self):
        pessoa = Pessoa ('001','Diogo','3','998845108','diogo.azvg@gmail.com')
        transporte = Transporte ('001','1001','www.1001.com.br','27338980','Rio','Bahia','R$ 3000')
        hotel = Hotel ('001','Softel Jequitimar','www.sbt.com.br','1127338977','R$ 300','3')
        refeicao = Refeicao('001','Le coco','www.lecoco.com.br','1127378977','5','R$ 67')
        pacote = Pacote ('001','022','003','004',pessoa)
        pacote.codPacote |should| equal_to ('001')
        pacote.codTransporte |should| equal_to ('022')
        pacote.codHotel |should| equal_to ('003')
        pacote.codRefeicao |should| equal_to ('004')

        pacote.pessoa |should| equal_to (pessoa)

    def it_inserir_pessoa_pacote(self):
        pessoas = Pessoa('001','Diogo','3','998845108','diogo.azvg@gmail.com')
        #pacote = Pacote('001', '022', '003', '004')
        
        #pacote = Pacote('001', pessoa)
       
        #pacote.it_inserir_pessoa_pacote(pessoa)
        #(pessoa in pacote.pessoas) |should| equal_to(True)
    
    
    def it_verificar_pessoa_pacote(self):
        pessoas = Pessoa('001','Diogo','3','998845108','diogo.azvg@gmail.com')
        #pacote = Pacote('001', '022', '003', '004')
        
       # codPessoa = Pessoa('001' ,'001', pessoa, pacote)
        
        #pacote.inserirCodPessoa(Pessoa)
        #pacote.verificaCodPessoas(Pessoa) |should| equal_to(True)


    def it_inserir_transporte_pacote(self):
        transp = Transporte('001','1001','www.1001.com.br','27338980','Rio','Bahia','R$ 3000')

    def it_verificar_transporte_pacote(self):
        transp = Transporte('001','1001','www.1001.com.br','27338980','Rio','Bahia','R$ 3000')


    def it_inserir_hotel_pacote(self):
        htl = Hotel('001','Softel Jequitimar','www.sbt.com.br','1127338977','R$ 300','3')

    def it_verificar_hotel_pacote(self):
        htl = Hotel('001','Softel Jequitimar','www.sbt.com.br','1127338977','R$ 300','3')


    def it_inserir_refeicao_pacote(self):
        refe = Refeicao('001','Le coco','www.lecoco.com.br','1127378977','5','R$ 67')

    def it_verificar_refeicao_pacote(self):
        refe = Refeicao('001','Le coco','www.lecoco.com.br','1127378977','5','R$ 67')







