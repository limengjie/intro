#!/usr/bin/env python
# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *
FILE_NAME = "shapes.txt"

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.


class Triangle(Shape):
    def __init__(self, base, height):
      self.base = float(base)
      self.height = float(height)
    def area(self):
      return self.base*self.height/2
    def __eq__(self, other):
      return type(other) == Triangle and self.base == other.base \
          and self.height == other.height
    def __str__(self):
      return 'Triangle with base '+ str(self.base) + ' and height '+ \
          str(self.height)

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.sqrCur = 0
        self.shapes = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        '''
        for e in self.shapes:
          if sh == e:
            return
        self.shapes.append(sh)
        '''
        for e in self.shapes:
          if sh == e:
            return
        if type(sh) == Circle:
          self.sqrCur += 1
          self.shapes.insert(0,sh)
        elif type(sh) == Square:
          self.shapes.insert(self.sqrCur, sh)
        elif type(sh) == Triangle:
          self.shapes.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        self.index = 0
        return self
    def next(self):
      if self.index >= len(self.shapes):
        raise StopIteration
      self.index += 1
      return self.shapes[self.index - 1]
    def __str__(self):
      return self.shapes[self.index - 1]
       
"""
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        
"""
        ## TO DO
       



#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    largeSh = []
    for shape in shapes:
      if largeSh == []:
        largeSh.append(shapes.shapes[0])
      elif shape.area() > largeSh[0].area():
        largeSh = [shape]
      elif shape.area() == largeSh[0].area() and\
      type(shape)!=type(largeSh[0]):
        largeSh.append(shape)
    return largeSh

ss1 = ShapeSet()
t3 = Triangle(2,36)
t0_eq = Triangle(3,4)
t0 = Triangle(3,4)
t1 = Triangle(2,3)
s0 = Square(5)
s1 = Square(6)
c = Circle(1)
ss1.addShape(s0)
ss1.addShape(t3)
ss1.addShape(t0_eq)
ss1.addShape(s1)
ss1.addShape(c)
ss1.addShape(t0)
ss1.addShape(t1)
print("=======================ss1.shapes=================================")
for e in ss1:
  print e

print ("=====================largest shape=============================")
largest = findLargest(ss1)
for e in largest:
  print e
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    ss2 = ShapeSet()
    FILE_NAME = "shapes.txt"
    inputFile = open(FILE_NAME)
    for line in inputFile:
      l = line.strip().split(",")
      if l[-1] == "circle":
        ss2.addShape(Circle(l[1]))
      elif l[0] == "square":
        ss2.addShape(Square(l[1]))
      elif l[0] == "triangle":
        ss2.addShape(Triangle(l[1],l[2]))
    print("===========================ss2.shapes========================")
    for e in ss2:
      print e
    print ("===================largest shape==========================")
    largest = findLargest(ss2)
    for e in largest:
      print e

readShapesFromFile(FILE_NAME)

