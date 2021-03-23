'''
Inheritance

Syntax:
class Base(object)
    Base_Body
Derived(Base)
    Derived_Body

'''

#Example 1
class Parent:
    pass
class Son(Parent):
    pass
print(issubclass(Son,Parent)) # issubclass(Derived_Class,Base_Class) : returns True

#Example 2
class Debian:
    def rel_date1(self):
        print("Debian was released on 1993")
class Ubuntu(Debian):# inheriting Debian class
    def rel_date2(self):
        print("Ubuntu was released on 2002")

a=Ubuntu() # calling derived class Ubuntu
a.rel_date1()
a.rel_date2()
'''
When we create an object of the derived class,
we invoke the constructor of the 
derived class which in turn calls
the base class constructor on the base class sub object.
'''


