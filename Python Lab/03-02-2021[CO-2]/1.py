n=int(input('Enter a number: '))
if n<0:
    print('Invalid input')
elif n==0 or n==1:
    print('Factorial is 1')
else:
    i=n-1
    while i>0:
          n=n*i
          i-=1
    print('Factorial is',n)