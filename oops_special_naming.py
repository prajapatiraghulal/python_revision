class Phone:
    def __init__(self,number, s_name,l_name, temp,temp1,get_var):
        self.number= number
        self.s_name = s_name
        self.l_name = l_name
        self.__temp = temp 
        self._temp1 = temp1
        self._get_var = max(get_var,0)   #for no negative
        self._add = self._get_var*2
    
    def make_a_call(self, number):
        print(f'calling {number}....')
    
    def full_name(self):
        return f'{self.s_name} {self.l_name} '
    
    @property   #this decorater allow us to use func name as attribute 
    def add(self):
        self._add = self._get_var*2
        return self._add
    
    #getter , setter
    @property       ##getter decorater 
    def get_var(self):
        return self._get_var
    
    @get_var.setter   ##setter , it should be declared after getter function only 
    def set_var(self,v):
        self._get_var = max(v ,0)
    



# _name # it indicate that variable is private but nothing is private in python it's just to tell the developer not to change value
# __name #(not a convention) # interpreter or compiler converts this internally in other form _className__name(we can access it like this) but not like __name
# __name__ # dunder/magic method

p1 = Phone(12345678,'rahul','roy','__temp','_temp',1000)
# print(p1.number, p1._temp1, p1.__temp)  #give error since there is not __temp its changed to _Phone__temp

# # print(p1.number, p1._temp1, p1._Phone__temp,p1._get_var p1._add)
# p1._get_var= -1000
# print(p1.number, p1._temp1, p1._Phone__temp,p1._get_var, p1._add)   #no chage in p1._add since it allocated once when constructor called only 
# #to handle above problem we can define setter() , and getter() type functions like separate func to p1._add initialization 

# # # print(p1.add())  #after using @property decorated it gives error as int object not callable since func name is treated as return object from func
# print(p1.number, p1._temp1, p1._Phone__temp,p1._get_var, p1._add) 
# print(p1.add )
# #now still we can give -ve value to p1._get_var to handle this 

p2 = Phone(333333,'mohan','lal','_','__',-5000)
print(p1._get_var, p2._get_var)

print(p1.get_var, p2.get_var)
p1.set_var= -1000
p2.set_var= 500
print(p1.get_var, p2.get_var)
print(p1.add, p2.add)
