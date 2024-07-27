from functools import reduce

alunos = [
    {'nome': 'pedro', 'nota': 8.5},
    {'nome': 'maria', 'nota': 9.2},
    {'nome': 'joao', 'nota': 7.6},
    {'nome': 'ana', 'nota': 6.8},
    {'nome': 'jose', 'nota': 5.3}
]

somar = lambda a, b: a + b

alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
total = reduce(somar, notas_alunos_aprovados, 0)

print(total / len(alunos_aprovados))

# Exemplo próprio - 

