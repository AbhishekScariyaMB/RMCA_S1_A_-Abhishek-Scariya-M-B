import circle
from rectangle import *
from Graphics._3D_graphics import cuboid,sphere
a=float(input('Enter length of the rectangle: '))
b=float(input('Enter breadth of the rectangle: '))
area(a,b)
r=float(input('Enter the radius of the circle: '))
circle.area(r)
l=float(input('Enter length of the cuboid: '))
b=float(input('Enter breadth of the cuboid: '))
h=float(input('Enter height of the cuboid: '))
cuboid.area(l,b,h)
r=float(input('Enter the radius of the sphere: '))
sphere.area(r)