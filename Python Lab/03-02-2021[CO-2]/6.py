txt=input('Enter a string: ')
s=set()
s.update(txt)
for i in s:
    c=0
    if i==' ':
        continue
    for j in txt:
        if i==j:
            c+=1
    print('Occurence of',i,'is',c)