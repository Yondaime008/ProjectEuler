def read_triangle(file):
   f = open(file, 'r')
   triangle = {}
   lines = f.read().splitlines()
   i=0
   for line in lines:
       A = line.split(' ')
       j=0
       for number in A:
       	triangle[i,j]=number
       	j=j+1
       i=i+1
   return triangle