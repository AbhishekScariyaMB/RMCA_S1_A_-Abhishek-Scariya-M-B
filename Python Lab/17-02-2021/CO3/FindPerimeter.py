import circle
from rectangle import *
from Graphics._3D_graphics import cuboid,sphere
a=float(input('Enter length of the rectangle: '))
b=float(input('Enter breadth of the rectangle: '))
perimeter(a,b)
r=float(input('Enter the radius of the circle: '))
circle.circumference(r)
l=float(input('Enter length of the cuboid: '))
b=float(input('Enter breadth of the cuboid: '))
h=float(input('Enter height of the cuboid: '))
cuboid.perimeter(l,b,h)
r=float(input('Enter the radius of the sphere: '))
sphere.perimeter(r)