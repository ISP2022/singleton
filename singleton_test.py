"""Example of using a Singleton as Metaclass.

To make a class into a singleton, 
    class ClassName(...,metaclass=Singleton)
"""
from singleton import Singleton


class Banknote(object): 
    # class variable to count instances
    _counter = 1
    
    def __init__(self):
        print(f"Performing Banknote constructor")
        self.name = f"Banknote #{Banknote._counter}"
        Banknote._counter += 1

    def __str__(self):
        return self.name



# Create some objects and test if they are the same object (singleton).
def test_singleton():
    print("Create 3 instances...")
    r1 = Banknote()
    r2 = Banknote()
    r3 = Banknote()

    print("\nPrint the instances...")
    print("r1 =", str(r1))
    print("r2 =", str(r2))
    print("r3 =", str(r3))

    print("\nCompare instances...")
    print("r1 is r2?", r1 is r2)
    print("r2 is r3?", r2 is r3)

if __name__ == "__main__":
    test_singleton()
