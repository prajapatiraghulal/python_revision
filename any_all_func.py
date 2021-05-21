'''any() func checks if any value is true in iterable and all() checks if all element
int iterable are true (ie any number other than 0 are true )'''

la=[1,2,3,0,2,-1,-4]
lb=[2,3,4,1,3,5,3,4]
print(any(la), any(lb))
print(all(la), all(lb))

print(any([a%2==0 for a in la]), all([a%2==0 for a in la]))
