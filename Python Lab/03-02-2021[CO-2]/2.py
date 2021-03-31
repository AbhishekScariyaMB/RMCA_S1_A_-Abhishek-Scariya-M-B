n=int(input('Enter number of terms:'))
a=0
b=1
print('First',n,'Fibonacci numbers:')
if n<=0:
    print('Invalid input')
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    i=3
    print(a)
    print(b)
    while i<=n:
        c=a+b
        print(c)
        a=b
        b=c
        i+=1