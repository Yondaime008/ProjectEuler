def read_triangle(file):
    f = open(file, 'r')
    triangle = {}
    lines = f.read().splitlines()
    for line in lines:

        return line

line = read_triangle('cipher.txt')
somme = 0
a = 103
b = 111
c = 100
i = 0
result = ''
for n in line.split(','):
    if i % 3 == 0:
        n = str(int(n) ^ a)
    elif i % 3 == 1:
        n = str(int(n) ^ b)
    else:
        n = str(int(n) ^ c)
    i += 1
    result += chr(int(n))
if 'the' in result or 'The' in result:
    for n in result:
        if n != '':
            somme += ord(n)
print(result)
print(somme)


