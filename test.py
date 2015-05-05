# class Point:
#    def __init( self, x=0, y=0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print(class_name, "destroyed")

# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
# del pt1
# del pt2
# del pt3


# class Block:
#     """Block is one of the many constituants of the castle"""
#     width = 0
#     height = 0
#     index = 0
#     def __init__(self, width, height, index):
#         super(Block, self).__init__()
#         self.width = width
#         self.height = height
#         self.index = index
# b1 = Block(1,10,13)
# print(id(b1),b1.width,b1.height,b1.index)

import itertools
from itertools import *

for j in combinations('ABCD', 1):
    print(j)

