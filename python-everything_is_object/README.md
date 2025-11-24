# Understanding Mutable vs Immutable Objects in Python!
One of the most important concepts in Python is knowing the difference between mutable and immutable objects. This affects how variables behave, how functions work, and why sometimes your code doesn’t do what you expect.

## Identity and Type
Every object in Python has an identity->id(), a type->type(), and a value.
- Identity tells us which object in memory we’re talking about.
- Type tells us what kind of object it is (list, int, str, etc.).
- Value is the actual data stored.

## Mutable vs Immutable
- Mutable objects: can be changed in place. Example: lists, dicts, sets.
- Immutable objects: cannot be changed once created. Example: ints, strings, tuples. Any “change” creates a new object.

### Examples
#### Integers (Immutable)
- Interning is when Python reuses the same object in memory for certain immutable values (like small integers and some strings).
- Instead of creating a new object every time you write 89, Python keeps a single copy and makes all variables point to it.
- This saves memory and speeds up comparisons.

```Python
a = 89
b = 89
print(a is b)  # True (small ints are interned)
```
#### Strings (Immutable)

- == compare values.
- is compares identities (same object in memory).
```Python
s1 = "BEST SCHOOL"
s2 = "BEST SCHOOL"
print(s1 == s2)  # True (same value)
print(s1 is s2)  # May be False (different objects in memory because of the space)
```
#### Lists (Mutable)

- The + creates a new object, while += mutates the existing one.
```Python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]   # creates a new list
print(l2)       # [1, 2, 3]
```
```
l1 = [1, 2, 3]
l2 = l1
l1 += [4]       # mutates in place
print(l2)       # [1, 2, 3, 4]
```

## Functions and Mutability
```Python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)  # [1, 2, 3, 4]
```
- Lists are mutable, so the function changes the original object.
```Python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # [1, 2, 3]
```

- Reassigning inside the function only changes the local variable n, not the caller’s variable.
```Python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1
```
- Integers are immutable. n+= 1 creates a new object, but a still points to the old one.
- To update a, you need to return the new value:
```Python
def increment(n):
    return n + 1

a = 1
a = increment(a)
print(a)  # 2
```

## Memory Hooks for remember
- Small ints and some strings → interned → is can be True.
- Tuples, lists, dicts → usually new objects → is is False unless explicitly reused.

### Example int and tuple
```Python
a = 1
b = 1
print(a is b)  # True

a = (1, 2)
b = (1, 2)
print(a is b)  # False (different tuple objects)
```

### Example for lists
- a += [...] → mutate in place → same id.
- a = a + [...] → new object → different id
```Python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
```Python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
## Why does this matter?
- Understanding mutability helps avoid bugs when passing objects to functions.
- It explains why some changes “stick” and others don’t.
- It clarifies the difference between value equality (==) and object identity (is).


