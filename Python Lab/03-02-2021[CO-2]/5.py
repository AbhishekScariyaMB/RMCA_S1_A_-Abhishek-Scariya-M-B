n=int(input('Enter the number of steps: '))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i*j,end=' ')
        j+=1
    i+=1
    print('\n')