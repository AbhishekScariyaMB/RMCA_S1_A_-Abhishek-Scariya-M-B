def file_read(fname):
    with open(fname) as f:
        # content_list is the list that contains the read lines.
        c=f.readlines()
        print(c)
        #print(len(c))


file_read("demo.txt")