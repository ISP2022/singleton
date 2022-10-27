## Singleton Metaclass for Creating Singletons

You can define a metaclass that intercepts calls to a class's
constructor and thereby control how many instances are created.

The `Singleton` class creates a map of class-to-instance
to provide singletons.

To make a class into a Singleton, use:

```python
from singleton import Singleton

class ClassName(object,metaclass=Singleton)
```

Test it.  Create multiple instances of your class:

```python
>>> m1 = SomeClass()
>>> m2 = SomeClass()
>>> m1 is m2
True
```
