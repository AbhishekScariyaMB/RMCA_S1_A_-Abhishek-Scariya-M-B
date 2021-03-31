num=[1,2,3,4,5,6,7,8,9,10,11,12]
num2=list()
for i in num:
    if(i%2!=0):
        num2.append(i)
print("Original list: "+str(num))
print("Even removed: "+str(num2))