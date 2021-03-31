txt=list(input('Enter words separated by space: ').split(' '))
big=0
for i in txt:
    if(len(i)>big):
        big=len(i)
print('Length of longest word: ',big)