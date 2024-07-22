print("--- variaveis.py ---")
a = 3
b = 4.4

print(a + b)

text = 'sua idade é...'
idade = 19

# print(text + str(idade))  # concatenação
# print(f'{text} {idade}')  # f-string

saudacao = 'bom dia'
print(3 * saudacao) 

pi = 3.14159265
raio = float(input('digite o raio da circuferencia: '))
area = pi * pow(raio, 2) # pow(raio, 2) == raio ** 2

print(f'a area da circuferencia é {area} m^2') 
print(type(raio)) 