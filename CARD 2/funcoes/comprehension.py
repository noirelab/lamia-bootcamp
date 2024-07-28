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
pilotos = [
    {'nome': 'hamilton', 'vitorias': 104},
    {'nome': 'shumacher', 'vitorias': 91},
    {'nome': 'verstappen', 'vitorias': 61},
    {'nome': 'vettel', 'vitorias': 53},
    {'nome': 'prost', 'vitorias': 51}
]

top3 = [piloto for piloto in pilotos if piloto['vitorias'] >= 54]

print(top3)
