import math
num=list()
for i in range(1000,10000):
    if (math.sqrt(i))-(math.floor(math.sqrt(i)))==0:
        j=i
        while j>1:
            r=int(j%10)
            if r%2!=0:
                break
            j=int(j/10)
            if(j==0):
                num.append(i)
print(num)