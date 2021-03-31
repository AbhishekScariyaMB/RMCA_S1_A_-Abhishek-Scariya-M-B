import math
n=int(input('Enter a number: '))
i=1
print('Factors are: ')
while i<=n:
    if(math.gcd(i,n)==i):
        print(i,' ',end='')
    i+=1