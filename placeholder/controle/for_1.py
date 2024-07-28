for i in range(10):         # 0 a 9
    print(i, end=' ')
print(' ')

for i in range(1, 11):      # 1 a 10
    print(i, end=' ')
print(' ')
    
for i in range(1, 100, 7):  # 1 a 100 de 7 em 7
    print(i, end=' ')
print(' ')

for i in range(20, 0, -3):  # 20 a 1 de -3 em -3
    print(i, end=' ')
print(' ')
    
nums = [2, 4, 6, 8]
texto = 'python eh daora!'

for n in nums:
    print(n, end=' ')
print(' ')
    
for letra in texto:
    print(letra, end=' ')
print(' ')

for n in {1, 2, 3, 4, 4, 4}: # tupla nao aceita repeticao
    print(n, end=' ')
print(' ')

produto = {
    'nome': 'caneta',
    'preco': 7.80,
    'desc': 0.5
}

for key in produto:
    print(f'{key} = {produto[key]}')
print(' ')
    
for key, valor in produto.items(): # pega chave e valor
    print(f'{key} = {valor}') 
print(' ')

for valor in produto.values(): # pega somente os valores
    print(valor)
print(' ')
    
for key in produto.keys(): # pega somente as chaves
    print(key)
    
# Exemplo próprio -
# Pares de 0 a 100
for i in range(1,20):
    if i % 2 == 0:
        print(i)