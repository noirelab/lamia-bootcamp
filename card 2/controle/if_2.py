a = 'valor'     # existe
a = 0           # nao existe
a = -0.00001    # existe
a = ''          # nao existe
a = ' '         # existe
a = []          # nao existe
a = {}          # nao existe

# print(not not 'valor')

if a:
    print('existe')
    
else:
    print('não existe ou zero ou vazio')