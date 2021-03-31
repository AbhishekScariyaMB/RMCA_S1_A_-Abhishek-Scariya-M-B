print('Find area of:- \n1.Square\t2.Rectangle\t3.Triangle')
ch=input('Enter choice: ')
if ch=='1':
    s=float(input('Enter side of square: '))
    ar=lambda s:s*s
    print('Area is:',ar(s),'sq.units')
elif ch=='2':
    a=float(input('Enter length of the rectangle: '))
    b=float(input('Enter breadth of the rectangle: '))
    ar=lambda a,b:a*b
    print('Area is:',ar(a,b),'sq.units')
elif ch=='3':
    b=float(input('Enter base of the triangle: '))
    h=float(input('Enter height of the triangle: '))
    ar=lambda b,h:0.5*b*h
    print('Area is: ',ar(b,h),'sq.units')
else:
    print('Invalid choice')