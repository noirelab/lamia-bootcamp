nota = float(input('informe a nota do aluno: ')) 
comportado = True if input('comportado? (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('parabens')
    print('quadro de honra')

elif nota >= 6:
    print('aprovado')

elif nota >= 4:
    print('recuperacao')

else:
    print('reprovado')

print(nota)