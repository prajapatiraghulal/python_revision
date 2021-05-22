from typing import Sized


class Person:
    count = 0
    def __init__(self):
        print(f'{self} created')
        Person.count+=1

    #class method
    @classmethod            #class method decorator   
    def count_func(cls):        #we give attribute as cls not class as class is for defining class so we use shortcut cls
        return f'object created = {cls.count} '


    #static method
    @staticmethod  #static method decorator 
    def static():   #static method does not take parameter of cls or self as it is static for class and all object
        return f'static method called'

        


p1 = Person()
# print(Person.count, p1.count)
p2 = Person()
p3 = Person()
# print(p1.count,p2.count, p3.count)
# print(p1.__dict__, p2.__dict__,Person.__dict__)
# print(Person.count)


#class method calling
print(Person.count_func())
print(p1.count_func())  #this is not right thing to do 

#static method calling
print(Person.static())


