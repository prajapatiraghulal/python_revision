#unique unordered collection of data
s = {1,2,6,3,2,9,5,5,'raja',1.2,1.0}
# print(s)
#print(help(s))
# s.add(32)
# s.add(900)
# print(s)
# print(s.remove(32), s)
#print(s.remove(222),s) #give error as keyerror
x = set(range(32))
print(len(x), x.__len__())
#print(x.clear(), x)
z = s.difference(x)
print(z)
#print(s.difference_update(x),s)
# print(z.discard('raja'), z.discard('raja'),z) #error proof
#print(z.issubset(s), z.issubset(x))
# print(z.pop(), z.pop(),z)
 ''