#Data types in Python are a way to classify data items.
# They represent the kind of value, which determines what operations can be performed on that data. 
# Since everything is an object in Python programming, 
# Python data types are classes and variables are instances (objects) of these classes.

# The following are standard or built-in data types in Python:

# Numeric: int, float, complex
# Sequence Type: string, list, tuple
# Mapping Type: dict
# Boolean: bool
# Set Type: set, frozenset
# Binary Types: bytes, bytearray, memoryview


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
