num=list()
num=input('Enter elements separated by space').split(' ')
sum=0
for i in num:
    sum+=int(i)
print('Sum: ',sum)