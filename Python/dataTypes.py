#Data types in Python are a way to classify data items.
# They represent the kind of value, which determines what operations can be performed on that data. 
# Since everything is an object in Python programming, 
# Python data types are classes and variables are instances (objects) of these classes.

# The following are standard or built-in data types in Python:

# Numeric: int, float, complex
# - int: Represents whole numbers (positive, negative, zero) without decimals.
# - float: Represents real numbers with decimal points or scientific notation.
# - complex: Represents numbers with a real and imaginary part (e.g., 2+3j).
#   Used in mathematical and scientific calculations involving complex numbers.

# Sequence Type: string, list, tuple
# - string (str): Ordered, immutable collection of characters.
#   Supports indexing, slicing, and many text manipulation operations.
# - list: Ordered, mutable collection of items (heterogeneous allowed).
#   Can grow or shrink dynamically; supports indexing and slicing.
# - tuple: Ordered, immutable collection of items.
#   Similar to lists but fixed in size and often used for fixed datasets.

# Mapping Type: dict
# - dict: Unordered, mutable collection of key-value pairs.
#   Keys must be immutable (e.g., str, int, tuple).
#   Provides fast lookup, insertion, and deletion.

# Boolean: bool
# - bool: Represents truth values → True or False.
#   Often the result of comparisons or logical operations.
#   Subclass of int (True = 1, False = 0).

# Set Type: set, frozenset
# - set: Unordered, mutable collection of unique items.
#   Useful for membership testing, eliminating duplicates, and set operations
#   (union, intersection, difference).
# - frozenset: Immutable version of set.
#   Can be used as dictionary keys or elements of another set.

# Binary Types: bytes, bytearray, memoryview
# - bytes: Immutable sequence of bytes (values in range 0–255).
#   Often used for raw binary data, files, and network communication.
# - bytearray: Mutable version of bytes.
#   Supports in-place modifications of binary data.
# - memoryview: Provides a view (or "window") of memory of other binary objects
#   without copying. Useful for efficient data handling.



# Numeric:

a = 5
print(type(a)) # <class 'int'>

b = 0.5
print(type(0.5)) # <class 'float'>

c = 5 + 2j
print(type(c)) # <class 'complex'>


# Sequence

a = list()
b = []
print(type(a),type(b)) # <class 'list'> <class 'list'>

c = str()
d = ""
print(type(c),type(d)) # <class 'str'> <class 'str'>

e = ()
f = tuple()
print(type(e),type(f)) # <class 'tuple'> <class 'tuple'>


# Mapping:

a = dict()
b = {"a": "Hello"}
print(type(a),type(b)) # <class 'dict'> <class 'dict'>

# Boolean:
a = False
b = True
print(type(a),type(b)) # <class 'bool'> <class 'bool'>

# Set type:
a = set()
b = {1,2,3,4}
c = {}
print(type(a),type(b), type(c)) # <class 'set'> <class 'set'> <class 'dict'>


# Binary Types: bytes, bytearray, memoryview

# bytes example
b = b"Hello"         # bytes literal
print(b)             # b'Hello'
print(type(b))       # <class 'bytes'>

# bytearray example
ba = bytearray(b"Hello")  # create from bytes
print(ba)                 # bytearray(b'Hello')
print(type(ba))           # <class 'bytearray'>

# memoryview with bytearray
data = bytearray(b"Python")
mv = memoryview(data)
print(type(mv))           # <class 'memoryview'>
