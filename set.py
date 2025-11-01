collection={1,2,3,4,5,"hello","hello"}
print(collection)
print(type(collection))
print(len(collection))


col1=set()#empty set syntax
print(type(col1))


#set methods

collection1=set()
collection1.add(1)
collection1.add(2)
collection1.add(3)
print(collection1)
collection1.remove(2)
print(collection1)
#collection1.clear()
#print(len(collection1))
print(collection.pop())



#union of set

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
