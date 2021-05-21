'''list, tuple etc are iterable and using iter(list obj) we get its iterator and doing
next(iter(list obj)) we get its element, while map,filter fn gives iterator object which
nex(map object) gives next element '''

la = [1,2,3,4]   #list is iterable 
ma = map(lambda s:s**2, la)    #map give map iterator object which can iterate once 

print(next(ma))
print(next(ma))
# for i in ma:
#     print(i)

#####print(next(la))   #will give error since list is iterable not iterator 
print(next(iter(la)))

it = iter(la)
print(next(it))
print(next(it))
print(next(it))

print(next(iter(la))) #iter initialize first address of list la


