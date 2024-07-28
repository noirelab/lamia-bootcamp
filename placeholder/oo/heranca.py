class Carro:
    def __init__(self):
        self.__velocidade = 0
        
    @property # caso queira acessar a velocidade, só carro.velocidade
    def velocidade(self):
        return self.velocidade    
        
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
    
class Uno(Carro):
    pass

class Ferrari(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()

c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())
print('')

# Exemplo próprio -
class Lamborghini(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()
    
cL = Lamborghini()
print(cL.acelerar())
print(cL.frear())