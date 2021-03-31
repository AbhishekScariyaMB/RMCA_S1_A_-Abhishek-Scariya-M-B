print("Enter a list of numbers separated by space: ")
txt=input()
list1=list()
list1=txt.split(" ")
print("Enter another list of numbers separated by space: ")
txt=input()
list2=list()
list2=txt.split(" ")
if(len(list1)==len(list2)):
    print("They have same length")
else:
    print("They have unequal length")
s1=s2=0
for i in list1:
    s1+=int(i)
for i in list2:
    s2+=int(i)
if(s1==s2):
    print("They add up to be equal")
else:
    print("They have unequal sum")
same=dict()
for i in list1:
    for j in list2:
        if(i==j):
            same[i]="Yes"
print("Common items: ")
for i in same.keys():
    print(i)




