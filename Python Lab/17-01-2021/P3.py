Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=float(input("Enter 1st number: "))
Enter 1st number: 12
>>> b=float(input("Enter 2nd number: "))
Enter 2nd number: 23
>>> c=float(input("Enter 3rd number: "))
Enter 3rd number: 99
>>> if(a>b)and(a>c):
	print(a,"is biggest")
elif(b>a)and(b>c):
	print(b,"is biggest")
else:
	print(c,"is biggest")

	
99.0 is biggest
>>> 