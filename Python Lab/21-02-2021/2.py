a=open('demo.txt','r')

b=open('t.txt','w')

c=a.readlines()

for i in range(0,len(c)):
    if(i%2 !=0):
        b.write(c[i])

    else:
        pass
b.close()

b=open('t.txt','r')
d=b.read()
print(d)
a.close()
b.close()