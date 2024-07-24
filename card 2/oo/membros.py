class Contador:
    contador = 10    # atributo de classe
    
    def inst(self):
        return 'Estou bem!'
    
    def inc_maluco(self):
        self.contador += 1
        return self.contador
    
    @classmethod
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