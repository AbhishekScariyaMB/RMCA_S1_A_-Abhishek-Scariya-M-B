import datetime
a=datetime.datetime.now()
a=int(a.year)
b=int(input("Enter final year: "))
print("\nLeap Years:")
for i in range(a,b+1):
    if(i%4==0):
        print(i)
