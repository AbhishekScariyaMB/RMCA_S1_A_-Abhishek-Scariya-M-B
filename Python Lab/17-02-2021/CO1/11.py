a=int(input('Enter 1st no: '))
b=int(input('Enter 2nd no: '))
c=int(input('Enter 3rd no: '))
if a>b and b>c:
    print(a,'is the biggest number')
elif b>a and b>c:
    print(b,'is the biggest number')
else:
    print(c,'is the biggest number')