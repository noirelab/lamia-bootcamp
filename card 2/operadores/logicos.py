b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3) # False
print(b1 or b2 or b3)   # True
print(b1 != b2 )        # True
print(not b1)           # False

print(b1 and not b2 and b3) # True

x = 3
y = 4

print(b1 and not b2 and x < y)  # True, operadores racionais com opradores logicos
print('')
# Exemplo próprio -
b2 = True
b4 = False
print(b1 and b2 and b3 and b1 and b2)
print(b1 and b2 and b3 and b1 and b2 and b4)