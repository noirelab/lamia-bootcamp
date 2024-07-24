from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc

# def mais_um_meio(nota):
#     return nota +1.5

notas = [6.4, 7.2, 5.8, 8.4]
notas_finais = map(somar_nota(1.5), notas) # map: consegue transformar uma lista em outra lista, ex: objeto -> string, string -> int
notas_finais2 = map(somar_nota(1.6), notas) 

print(list(notas_finais))
print(list(notas_finais2))

# total = 0
# for n in notas:
#     total += n
# print(total)

def soma(a,b):
    return a + b

total = reduce(soma, notas, 0) # reduce: consegue transformar uma lista em um único valor, ex: soma de todos os elementos da lista
print(total)

# for i, nota in enumerate(notas):
#     notas[i] = nota +1.5
    
# for i in range(len(notas)):
#     notas[i] = notas[i] +5