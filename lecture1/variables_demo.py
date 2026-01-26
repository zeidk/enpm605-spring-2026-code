
# Object Types in Python
# -------------------------------------------------------------
print(type(10))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(print))  # <class 'builtin_function_or_method'>

# The id() Function
# -------------------------------------------------------------
a = 10
b = 10.5
c = "hello"

print(id(a))  # e.g., 9793376
print(id(b))  # e.g., 140409546886992
print(id(c))  # e.g., 140409536180784

# What about literals?
print(id(10))  # Same as id(a)?
print(id("hello"))  # Same as id(c)?

# Dynamic Typing in Python
# -------------------------------------------------------------
x = "hello"
print(type(x))  # <class 'str'>

x = 10.5
print(type(x))  # <class 'float'>


# Immutability vs Mutability
# -------------------------------------------------------------
x = 10
print(id(x))  # 9793376

x = x + 1  # New object created!
print(id(x))  # 9793408 (different)

my_list = [1, 2, 3]
print(id(my_list))  # 140234567890

my_list.append(4)  # Same object!
print(id(my_list))  # 140234567890 (same)

# Aliasing and Object References
# -------------------------------------------------------------
a = [1, 2, 3]
b = a  # b references same list

print(id(a))  # e.g., 140234567890
print(id(b))  # Same address!
print(a is b)  # True

b.append(4)
print(a)  # [1, 2, 3, 4] -- both changed!

# The None Object
# -------------------------------------------------------------
# Declaring a variable with no value yet
result = None


# Function that doesn't explicitly return anything
def greet(name):
    print(f"Hello, {name}")


x = greet("Alice")  # Prints "Hello, Alice"
print(x)  # None
print(type(x))  # <class 'NoneType'>


# is vs == Operator
# -------------------------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True  (same values)
print(a is b)  # False (different objects)
print(a is c)  # True  (same object)

# The print() Function
# -------------------------------------------------------------
# Print literals
print("Hello")  # Hello
print(3)  # 3
print(2.4)  # 2.4

# Print expressions
print(2 + 3)  # 5
print("*" * 10)  # **********

# Multiple arguments (separated by space by default)
print("Welcome", "to", "ENPM", 605)  # Welcome to ENPM 605

# Custom separator and end
print("a", "b", "c", sep="-")  # a-b-c
print("No newline", end="")  # No newline after