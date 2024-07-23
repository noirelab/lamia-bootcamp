def saudacao(nome = 'pessoa', idade = 20):
    print(f'bom dia {nome}')
    print(f'voce tem {idade} anos')
    
# def saudacao():
#    print('boa tarde')

def soma_e_multi(a, b, x):
    return a + b * x

if __name__ == '__main__': # só executa se for o arquivo principal
    saudacao('ana', idade = 30)