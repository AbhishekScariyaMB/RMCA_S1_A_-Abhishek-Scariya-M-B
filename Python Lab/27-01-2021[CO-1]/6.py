names=["Akash","Alazka","Leonardo","Margot","Amanda"]
c=0
for i in names:
    for j in i:
        if(j=='a'):
            c+=1
print(names)
print("Number of a is "+str(c))