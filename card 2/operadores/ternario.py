lockdown = False
grana = 30

status = 'em casa' if lockdown or grana <= 100 else 'uhu' 

print(status)