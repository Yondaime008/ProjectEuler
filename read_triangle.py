def read_triangle(file):
    f = open(file, 'r')
    triangle = {}
    lines = f.read().splitlines()
    i = 0
    for line in lines:
        a = line.split(' ')
        j = 0
        print(a)
        for number in a:
            triangle[i, j] = number
            j += 1
        i += 1
    return triangle

triangle = read_triangle('triangle.txt')

i = 0
somme = 0
while i < 16:
    somme += triangle[i, j]