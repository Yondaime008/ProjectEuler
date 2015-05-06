"""
a,b<100 what is the values of a, b that have the maximum sum of elements
"""

maximum = 0

for a in range(1,101):
    for b in range(1,101):
        somme=0
        for c in str(a**b):
            somme += int(c)
        if somme>maximum:
            maximum = somme
            index_a = a
            index_b = b
print(index_a, index_b, maximum)