"""
Define a singleton class using a Meta-Class.
"""

class Singleton(type):
    """A Meta-class for making a class into a singleton.
       The __call__ method intercepts calls to class's constructor,
       and returns a singleton instance of the class.

       Usage: class MyClass(BaseClass, metaclass=Singleton):
    """
    # A dictionary of classes for which a Singleton instance exists,
    # so that Singleton can be the metaclass of several classes.
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
