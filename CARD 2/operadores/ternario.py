lockdown = False
grana = 30

status = 'em casa' if lockdown or grana <= 100 else 'uhu' 

print(status)

# Exemplo próprio -
status1 = 'triste' if lockdown or grana <= 100 else 'feliz'