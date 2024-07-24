class Produto:
    def __init__(self, nome, preco = 1.99, desc = 0):
        self.nome = nome   
        self.__preco = preco
        self.desc = desc
        
    @property
    def preco(self):
        return f'R$ {self.__preco}'
    
    @preco.setter # muda a variável privada
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        
    @property # um método vira uma váriavel na hora de chamar
    def preco_final(self):
        return (1 - self.desc) * self.__preco
        

p1 = Produto('caneta', 10, 0.1) # produto.__init__(p1)
p2 = Produto('caderno', 14, 0.5)

p1.preco = 70       # usa o getter (property) pra ler e setter pra mudar
p2.preco = 17.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)