#Slicing
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[0:3])  # First three elements
print(list[3:])   # All elements after the first three
print(list[:3])   # First three elements
print(list[-3:])  # Last three elements
print(list[::2])  # Every second element
print(list[::-1])  # Reverse the list
# Unpacking
a, b, c, *rest = list
print(a)      # 1
print(b)      # 2
print(c)      # 3
print(rest)   # [4, 5, 6, 7, 8, 9]
# Unpacking with asterisk
a, b, *rest = list[:5]  # Unpacking first five elements
print(a)      # 1
print(b)      # 2
print(rest)   # [3, 4, 5]
# Unpacking with asterisk and multiple variables
a, *rest, b = list  # Unpacking with asterisk at the beginning and end
print(a)      # 1
print(rest)   # [2, 3, 4, 5, 6, 7, 8]
print(b)      # 9
# Unpacking with asterisk and multiple variables in reverse order
a, *rest, b = list[::-1]  # Unpacking in reverse order
print(a)      # 9
print(rest)   # [8, 7, 6, 5, 4, 3, 2]
print(b)      # 1
# Unpacking with asterisk and multiple variables in reverse order with slicing
a, *rest, b = list[-3:]  # Unpacking last three elements
print(a)      # 7
print(rest)   # [9]
print(b)      # 9
# Unpacking with asterisk and multiple variables in reverse order with slicing
a, *rest, b = list[:3]  # Unpacking first three elements
print(a)      # 1
print(rest)   # [2]
print(b)      # 3
