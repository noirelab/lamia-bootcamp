from functools import reduce

alunos = [
    {'nome': 'pedro', 'nota': 8.5},
    {'nome': 'maria', 'nota': 9.2},
    {'nome': 'joao', 'nota': 7.6},
    {'nome': 'ana', 'nota': 6.8},
    {'nome': 'jose', 'nota': 5.3}
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7 
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

alunos_aprovados = filter(aluno_aprovado, alunos) # filter(função, lista) # remove os dois q nao atenderam a condição
nota_alunos_aprovados = map(obter_nota, alunos_aprovados)
total = reduce(somar, nota_alunos_aprovados, 0)

print(total / len(list(alunos_aprovados)))

# print(list(nota_alunos_aprovados))
# print(obter_nota(alunos[2]))
# print(alunos)
# print(list(alunos_aprovados))