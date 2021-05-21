# '''#tuple does not support remove delete pop 
# #tuples are immutable and similar to list'''

# # tpl = ('ram',3,'shyam')
# # print(tpl)
# # print(tpl[0:2:1])

# # ek = (3)
# # print(type(ek))
# # do = (3,)
# # print(type(do,))

# # ttpl = 3,'ram','shyam',3.4       #default tuple
# # print(type(ttpl))
# # print(ttpl)

# # x,y,z,w = ttpl
# # print(x,w)

# #list inside tuple can be mutable 
# tppl = (3,'ram',[1,2,3])
# tppl[2].append('maharaj')
# print(tppl)

# zz = (1,2,4,2)
# #fn on tuple
# print(max(zz))

# #multiple comma separated return are returned as tuple
# def summ(a,b):
#     su = a+b
#     mu = a*b
#     return su,mu 
# print(type(summ(3,4)))

#conversion from tup to list and string
tpp = (1,2,3,4)
lst = list(tpp)
st = str(tpp)
print(type(lst), lst)
print(type(st), st, st[0])
