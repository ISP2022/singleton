"""
Define a singleton class using a Meta-Class.
"""

class Singleton(type):
    """A Meta-class for making a class into a singleton.
       The __call__ method intercepts calls to class's constructor,
       and returns a singleton instance of the class.

       Usage: class MyClass(BaseClass, metaclass=Singleton):
    """
    # A dictionary of classes for which a Singleton instance exists.
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # call the class's constructor
            the_singleton = super(Singleton, cls).__call__(*args, **kwargs)
            # add it to the dict of known classes & their singletons
            cls._instances[cls] = the_singleton
        return cls._instances[cls]
