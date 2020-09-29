
# Data structures:
#   1. Lists / arrays
#   2. Sets
#   3. Dictionaries


# Lists
lst = [1, 1, 11, 7]
print("Original List:", end=" ")
print(lst)

lst.append(15)
print("Append '15':", end=" ")
print(lst)

lst.remove(11)
print("Remove '11':", end=" ")
print(lst)

lst.sort()
print("Sorted:", end=" ")
print(lst)
print()

# Sets
st = {1, 1, 11, 7}
print("Original Set:", end=" ")
print(st)

# sets are all about distinct items (no duplicates)
st.add(1)
st.add(11)
print("Added '1' and '11':", end=" ")
print(st)
print("...but the set didn't change")
print()


#Dictionaries
d = {
    'bob': 0,
    'sarah': 0,
}

print("Print dictionary:")
print(d)
print("Bob's score:",end=" ")
print(d['bob'])

d['bob'] += 1
print("Adding '1' to Bob's score:", end=" ")
print(d['bob'])

d['michael'] = 7
print("Giving Michael a score of '7':", end=" ")
print(d['michael'])
