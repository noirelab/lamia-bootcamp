from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]

for i, nota in enumerate(notas):
    notas[i] = nota + 1.5
    
print(notas)