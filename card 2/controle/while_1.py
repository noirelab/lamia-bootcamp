x = 0
nota = 0
qtd = 0

while nota != -1:
    nota = float(input('informe a nota ou -1 para sair: '))
    if nota != -1:
        qtd += 1
        x += nota
    
print(f'a media é {x/qtd:.2f}')

x = 10


""" 
while x:
    print(x)
    x -= 1 
    
print('fim')
""" # for baixa renda

# Exemplo próprio -
answer = 0
while answer != 5:
    answer = int(input('digite 5 para encerrar'))