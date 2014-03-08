class Pacote:
    def __init__ (self,codPacote,codTransporte=[None],codHotel=[None],codRefeicao=[None],pessoa=[None]):
        self.codPacote = codPacote
        self.codTransporte = codTransporte
        self.codHotel = codHotel
        self.codRefeicao = codRefeicao
        self.pessoa = pessoa

    def inserirCodPessoa(self,pessoas):
        self.pessoa.append(pessoas)
    def verificaCodPessoas(self,pessoas):
        return codPessoa in self.pessoa

    def inserirCodTransporte(self,transp):
        self.codTransporte.append(transp)
    def verificaCodTransporte(self,transp):
        return codTransporte in self.transporte

    def inserirCodHotel(self,transp):
        self.codTransporte.append(transp)
    def verificaCodPessoas(self,transp):
        return codPessoa in self.transporte
