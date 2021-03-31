import csv
with open('dep.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for r in d:
        print(','.join(r))