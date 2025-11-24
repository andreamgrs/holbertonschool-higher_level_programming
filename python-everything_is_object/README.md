# Understanding Mutable vs Immutable Objects in Python!
One of the most important concepts in Python is knowing the difference between mutable and immutable objects. This affects how variables behave, how functions work, and why sometimes your code doesn’t do what you expect.

## Identity and Type
Every object in Python has an identity->id(), a type->type(), and a value.
- Identity tells us which object in memory we’re talking about.
- Type tells us what kind of object it is (list, int, str, etc.).
- Value is the actual data stored.

## Mutable vs Immutable
- Mutable objects: can be changed in place. **Example:** lists, dicts, sets.
- Immutable objects: cannot be changed once created. **Example:** ints, strings, tuples. Any “change” creates a new object.

### Examples
#### Integers (Immutable)
- In memory: x points to the integer object 5, then x += 1 creates a new integer object 6 and reassigns x to point to it. So the original 5 object is untouched.
- That’s why integers and strings behave differently from lists: they don’t mutate, they get replaced.
```Python
x = 5
print(id(x))   # memory address of 5
x += 1
print(id(x))   # different address, now pointing to 6
```

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
```Python
l1 = [1, 2, 3]
l2 = l1
l1 += [4]       # mutates in place
print(l2)       # [1, 2, 3, 4]
```
## Assignment vs Referencing
- Assignment: is for example when you write **a = 10**, Python creates an object (10) and makes the variable a point to it.
- Referencing: is for example when you write **b = a**, you’re not copying the object, you’re making b point to the same object as a.

## Passing Variables to Functions (By Assignment)
Python uses a model often described as **call by object reference** or **call by assignment.**
- When you pass a variable to a function, Python passes a reference to the object the variable points to.
- Inside the function, the parameter becomes a new variable pointing to the same object.
- Whether changes persist depends on mutability.

### Example with a mutable object (list)
In this example:
- The function receives a reference to the same list.
- Since lists are mutable, the change persists outside the function.
```Python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)  # [1, 2, 3, 4]
```

- Reassigning inside the function only changes the local variable n, not the original variable.
```Python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # [1, 2, 3]
```

### Example with an immutable object (int)
- Integers are immutable. n+= 1 creates a new object, but a still points to the old one.
```Python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1
```

- To update a, you need to return the new value:
```Python
def increment(n):
    return n + 1

a = 1
a = increment(a)
print(a)  # 2
```

### Memory Hooks for remember
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
- Tuples and frozensets are immutable, so once created, their structure (the sequence of items in a tuple, or the membership of a frozenset) cannot be changed.
#### How tuples and frozen set works? 
- When atuple or frozenset is created, Python stores references (aliases) to the objects inside.
- If those objects are mutable (like lists or dict), we can modify the contents of those objects, even though the tuple or frozenset won’t let replace or reorder the references.

**Example Tuple**
```Python 
list = [1, 2]
t = (list, 3)

print(t)        # ([1, 2], 3)
list.append(4)
print(t)        # ([1, 2, 4], 3)  <-- tuple unchanged, but list inside mutated
```

**Example Frozen Set**
- A frozenset doesn’t store the actual objects directly; it stores references (pointers) to them.
```Python 
list = [1, 2]
fs = frozenset([id(list)])  # store reference via id
list.append(3)
print(list)  # [1, 2, 3]
# frozenset still contains the same reference, but the object it points to has changed
```

### Example for lists and identity (id)
- a += [...] → mutate in place → same id.
- a = a + [...] → new object → different id
```Python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a) # Not the same id 
```
```Python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a) # Same id
```
## Integer Pre‑Allocation in CPython
When CPython starts, it pre‑allocates a range of integer objects so they can be reused. This is an optimization for speed and memory efficiency.

The range
- CPython creates all integers from -5 to 256 at startup.
- These are stored in memory and reused whenever you reference them.
- That’s why:
```Python
a = 100
b = 100
print(a is b)   # True -> Both a and b point to the same pre‑allocated integer object.
```
### Aliases and Identity
- In Python, names are aliases for objects. When we assign a variable we are creating a new reference (alias) to it.
- For immutable objects (like integers, strings, and tuples), this aliasing is safe because the object itself can’t be changed.
- For mutable objects (like lists or dicts), aliasing means multiple names can point to the same object.
```Python
x = 42
y = x   # y is now an alias for the same int object
print(x is y)  # True
```
### NSMALLPOSINTS and NSMALLNEGINTS
These are **compile-time constants** defined in CPython’s source code (Include/internal/pycore_object.h):
- **NSMALLPOSINTS = 257** covers integers from 0 to 256
- **NSMALLNEGINTS = 5** covers integers from -1 to -5
Together, they define the range of pre-allocated integers.

CPython pre-allocates small integers because they are used constantly in programs, such as for loop counters, indexes, and flags. 
- By reusing these objects instead of creating new ones each time, Python avoids repeated memory allocation and deallocation, which improves:
 - performance and efficiency. 



