class Laptop:
    disc=10     #class variable
    def __init__(self,name,price):          #constructor
        #instance variables
        self.name = name
        self.price = price
    
    def discount(self):
        return (self.price-self.price/100.0)*self.disc      #self.disc is for instance only and can be used for all and for specific variable also

l1= Laptop('asus z',32000)
l2= Laptop('hp',70000)

print(l1.name,',',l2.name)
# # # # # # # # print(Laptop.__init__(l1,'ram','shyam'),l1.name)  #inside calling of instance function
print(l1.name)

print(l1.discount(), l2.discount())
print(Laptop.discount(l1), Laptop.discount(l2))  #this is similar to just above code this is actually done by interpreter internally 

# l=[1,2,3]
# list.clear(l)
# print(l)

print(l1.__dict__, l2.__dict__)

l3= Laptop('dell', 65000)
l3.disc = 20
print(l3.__dict__, l3.discount())


###we can define specific instance variable which is not defined 
# l2.new_name = 'dell new'
# print(l2.__dict__)
