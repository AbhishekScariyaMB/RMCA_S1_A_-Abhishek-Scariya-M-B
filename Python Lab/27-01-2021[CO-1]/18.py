dict1={"Name":"Cassandra","Age":23,"Sex":"Female"}
dict2={"Occupation":"Assassin","Agency":"XR8"}
print("Dictionary 1: "+str(dict1))
dict1.update(dict2)
print("Dictionary 2: "+str(dict2))
print("Merged dictionary: "+str(dict1))