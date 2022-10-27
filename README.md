## Singleton Metaclass for Creating Singletons

You can define a metaclass that intercepts calls to a class's
constructor and thereby control how many instances are created.

The `Singleton` class creates a map of class-to-instance
to provide singletons.

To apply it to some class use:
```python
from singleton import Singleton

class ClassName(object,metaclass=Singleton)
```
