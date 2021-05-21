dct = {3:'ram', 'mohan':4, 4.24:[8,34,'raja']}
# print(dct['mohan'])
# print(dct[4.24])

# dt = dict(mahannn='nana', mohan=4.5, sohan=34)
# print(dt)

# dct['new']= 'rahulroy'
# print(dct)

# if 'ram' in dct:
#     print('present')
# else:
#     print('absent')


# if 'ram' in dct.values():
#     print('present')
# else:
#     print('absent')

# #loop
# for i in dct:
#     print(i)
# for i in dct.values():
#     print(i)

# for i in dct.items():  #.items() returns tuple of key_value pair, .keys(), .values()
#     print(i)
# print(dct.pop(3), dct) 
# print(dct.popitem(),dct) #removes item from last and returns tuple of k_v pair

# #update method
# dd = {1:89,'mohan':100000}
# dct.update(dd)      #similar key will get updated and other get appended
# print(dct)   

##print(dir(dct))

# print(dict.fromkeys([1,2,'raja'],'abcd')) # fromkeys creates new dict with values same for all keys
# print(dct)

#get can be used to get value using key and it handles key error 
# print(dct.get(3))
# print(dct.get(2))   #will not give error but give none which is false

# d= dct
# d1= dct.copy()
# print(d is dct, d1 is dct)

# print(dct.get(2,'not found!'))  #we can use default not found return value in 2nd param
