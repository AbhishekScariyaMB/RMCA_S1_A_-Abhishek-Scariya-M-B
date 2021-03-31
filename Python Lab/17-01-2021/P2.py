Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Area(r):
	pi=3.14
	return pi*r*r

>>> r=float(input("Enter the radius: "))
Enter the radius: 3
>>> area=Area(r)
>>> print("The area is:",area,"sq.units")
The area is: 28.259999999999998 sq.units
>>> 