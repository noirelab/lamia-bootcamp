pessoas = ['Gui', 'Rebeca']
adj = ['Sapeca', 'Inteligente']

# O^2
for p in pessoas: 
    for a in adj:
        print(f'{p} é {a}!')
        
for i in [1, 2, 3]:
    pass # laço vazio

for i in range(1, 11):
    if i % 2 == 1:
        continue # so vai entrar aqui se for par
    print(i, end=' ')    
print('')

for i in range(1, 11):
    if i == 5:
        break # quebra o laço
    print(i, end=' ')
    
print("")

# Exemplo próprio -
for i in range(0, 10):
    if i % 2 == 1:
        print(f'{i} é impar')