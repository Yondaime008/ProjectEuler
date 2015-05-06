"""
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""
"""
n!
r!(n−r)!

"""
import math
somme = 0
for n in range(1,101):
    for r in range(1, n):
        if math.factorial(n)/(math.factorial(r)*math.factorial(n-r))>10**6:
            somme += 1
print(somme)