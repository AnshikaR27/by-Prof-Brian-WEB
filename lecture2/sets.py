# create an empty set:

s = set()

# add elements to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
# Even if you add three twice the set is still the same, kyuki yeh set hai isme there are no repetitive values stored.
# adding a repetitve element to the set
s.add(3)
print(s)

# removing an element from the set
s.remove(2)
print(s)

# giving out the length or say the number of elements in the set as o/p.
print(f"The set has {len(s)} elements." )