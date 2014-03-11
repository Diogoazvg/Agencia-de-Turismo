class Transporte:
    def __init__ (self,codTransporte,cia,site,telefone,origem,destino,precoViagem):
        self.codTransporte = codTransporte
        self.cia = cia
        self.site = site
        self.telefone = telefone
        self.origem = origem
        self.destino = destino
        self.precoViagem = precoViagem
    
    def update(self, cia, site, precoViagem):
    	self.cia = cia
    	self.site = site
    	self.precoViagem = precoViagem 
