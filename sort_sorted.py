'''obj.sort() sorts iterable and changes element order but sorted(iterable, key=func)
sorts acc to func and returns sorted list for tuple and set also '''

la =[3,2,4,1]
ta=tuple(la)
sa=set(la)
print(la,ta,sa)

print(la.sort(), la) 
#sorted func
print(sorted(la), sorted(ta), sorted(sa))
#print(help(sorted))

print(sorted(la, key=lambda s:s if s%2==0 else -s, reverse=False))