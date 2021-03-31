N=int(input("Enter N: "))
i=1
n=list()
sq=list()
while(i<=N):
    a=int(input("Enter "+str(i)+"th number:"))
    n.append(a)
    sq.append(a**2)
    i+=1
print("Numbers: "+str(n))
print("Squares: "+str(sq))

