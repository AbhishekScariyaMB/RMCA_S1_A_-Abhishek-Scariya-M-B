txt=str(input("Enter a line of text"))
words=txt.split(" ")
c=dict()
for i in words:
    c[i]=0
    for j in words:
        if(i==j):
            c[i]+=1
print("Occurences:-")
for i,j in c.items():
    print(i+":"+str(j))