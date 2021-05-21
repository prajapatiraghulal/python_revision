'''zip func give zip iterator object which creates tuple of items from all list in parameter
, smallest list item decide total zips 2,3---> 2,2'''

# la =['u1','u2','u3']
# lb = ['rahul','mohul']

# print(zip(la,lb))
# print(next(zip(la,lb)))
# print(list(zip(la,lb)))


# lc = [('a',1),('b',2)]   #this type of list can be converted to dict directly
# da = dict(lc)
# print(da)

# #so zip object for two list or tuple can be converted to dict directly
# db = dict(zip(la,lb))
# print(db)

ld = [(1,2,3),(4,5,6),(7,8,9)]
# print(*ld)
# print(list(zip(*ld)))



# # def func(*args):
# #     # print(args)
# #     la=list(zip(*args))
# #     # print(la)
# #     lb= [sum(a)/len(a) for a in la]
# #     return lb
# # print(func(*ld))

lamb= lambda *args:[sum(i)/len(i) for i in zip(*args)] 
print(lamb(*ld))

