class Contador:
    contador = 10    # atributo de classe
    
    def inst(self):
        return 'Estou bem!'
    
    def inc_maluco(self):
        self.contador += 1
        return self.contador
    
    @classmethod # construtor da nossa classe
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    @staticmethod
    def mais_um(n):
        return n+1
    
c1 = Contador()
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())

print(Contador.inc())
print(Contador.inc())
# print(Contador.inc())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.mais_um(99))

# Exemplo próprio -
class VrumVrum():
    def __init__(self):
        pass

    def vrum(self, text):
        print(text)

    @classmethod
    def vrumVrum(cls, text):
        print(text)

# VrumVrum.vrum("Vrum") nao vai executar
VrumVrum.vrumVrum("Vrum Vrum!") # vai executar pois o @classmethod deixa funcionar quando não tá instanciada
    