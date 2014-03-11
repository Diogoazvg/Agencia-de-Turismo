class Refeicao:
    def __init__ (self,codRefeicao,restaurante,site,telefone,quantRefeicao,precoKg):
        self.codRefeicao = codRefeicao
        self.restaurante = restaurante
        self.site = site
        self.telefone = telefone
        self.quantRefeicao = quantRefeicao
        self.precoKg = precoKg
    
    def update(self, refeicao, site, precoKg):
    	self.refeicao = refeicao
    	self.site = site
    	self.precoKg = precoKg 