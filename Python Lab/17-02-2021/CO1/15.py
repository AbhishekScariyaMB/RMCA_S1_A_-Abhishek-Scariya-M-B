colors1=set((input('Enter colors separated by commas: ')).split(','))
colors2=set((input('Enter colors separated by commas: ')).split(','))
print('Colors in color-list1 not contained in color-list2 are: ',list(colors1.difference(colors2)))