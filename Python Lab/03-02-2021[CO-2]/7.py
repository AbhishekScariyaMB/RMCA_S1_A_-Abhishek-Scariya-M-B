txt=input('Enter a string: ')
if txt[len(txt)-3:]=='ing':
    txt=txt+'ly'
else:
    txt=txt+'ing'
print('New text: '+txt)