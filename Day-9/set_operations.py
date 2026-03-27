# Creating dictionary and checking type
s = {}
print(type(s))   # dict

# Creating set
s = set()
s = {5678, 1234, 3456, 6789, 456, 34521}
print(s)

# Adding elements
s.add(124)
print(s)

# Removing element (only if exists)
# s.remove(123)  
s.remove(124)
print(s)

# Adding different data types
s.add(12.4)
s.add("string")
s.add(2+3j)
s.add(False)   
print(s)

# Membership check
print(False in s)

# Adding more elements
s.add(1)
print(s)

# Update multiple elements
s.update({2, 3, 4, 5})
print(s)

# Pop elements (random removal)
print(s.pop())
print(s.pop())

# Remove & discard
s.remove(2)      # removes 2
s.discard(3)     # removes 3 (no error if not present)
print(s)

# Loop through set
print("\nElements in set:")
for i in s:
    print(i)

# Set operations
a = {2, 34, 5, 6}
b = {3, 34, 5, 2}

print("\nIntersection:", a & b)
print("Union:", a | b)
print("Difference:", a - b)

# Subset and Superset
print({2} < a)   # subset
print({2} > a)   # superset

# Disjoint
print(a.isdisjoint(b))
print({0}.isdisjoint(a))