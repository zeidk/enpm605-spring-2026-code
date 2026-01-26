a = [1, 2, 3]
b = a  # b references same list

print(id(a))  # e.g., 140234567890
print(id(b))  # Same address!
print(a is b)  # True

b.append(4)
print(a)  # [1, 2, 3, 4] -- both changed!
