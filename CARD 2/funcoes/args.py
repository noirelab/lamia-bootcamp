def soma(*nums): # *nums = tupla
    total = 0
    for n in nums:
        total += n
        
    return total

def resultadoFinal(**kwargs): # **kwargs = dicionário
    status = 'aprovado' if kwargs['nota'] >= 6 else 'reprovado'
    
    return f'{kwargs["nome"]} foi {status}'

    # print(kwargs['nome'])
    # print(kwargs['nota'])
    
# Exemplo próprio -
def subtrair(*nums):
    inicial = 0
    for n in nums: 
        inicial -= n
        
    return inicial