import csv
with open('dep.csv', newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("ID  Department Name")
    print("--------------------------")
    for r in d:
        print(r['value'], r['data'])