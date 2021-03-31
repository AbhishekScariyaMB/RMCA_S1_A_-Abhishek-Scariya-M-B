import csv

field_names = ['best_book_id', 'authors', 'original_title']

book = [
    {
'best_book_id':1, 'authors':'Suzanne Collins', 'original_title':'	The Hunger Games'
    },
 {
'best_book_id':2, 'authors':'J.K. Rowling, Mary GrandPré', 'original_title':'	Harry Potter and the Philosophers Stone'
    },
 {
'best_book_id':3, 'authors':'Stephenie Meyer', 'original_title':'Twilight'
    },
]

with open('c1.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(book)

with open('c1.csv',newline='') as csvfile:
    d = csv.reader(csvfile,delimiter='|')
    for r in d:
        print(','.join(r))
