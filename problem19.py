CC = 19
DD = 1
somme = 0
for YY in range(1, 100):
    for MM in range(1, 13):
        if(CC//4-2*CC-1+5*YY//4+26*(MM+1)//10+DD) % 7 == 0:
            somme += 1

CC = 20
YY = 00
DD = 1
for MM in range(1, 13):
    if(CC//4-2*CC-1+5*YY//4+26*(MM+1)//10+DD) % 7 == 0:
            somme += 1

print(somme)