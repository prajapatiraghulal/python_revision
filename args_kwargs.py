# ''' * operator unpacks list ,set  and tuple and * takes all arguments to make them single tuple parameter '''
# # def sum(num1, *args):
# #     print(num1)
# #     print(type(args),args)

# # sum(4,3,2,3,4)
    
# def multiply(*args):
#     num=2
#     for i in args:
#         num*=i
#     return num

# # print(multiply(3,2,4), multiply())

# la = [3,2,1,4]
# # print(multiply(la))
# # print(*la)
# # print(multiply(*la))

# lb = {1,2,3,2,4,2,45}
# lc = {1:3, 2:4, 'r':'a'}
# print(*lb)
# print(*lc)
# #a,b,c = (*lc)  #cant use starred expression here
# a,b,c= tuple([*lc])
# print(type(c), c, type(b),b)

##########################################################################################################
#kwargs **
#** deals in dictionary same as * deals with tuple 

def kwar(**kwargs):
    print(type(kwargs))
    for i,j in kwargs.items():
        print(f'{i}:{j}')
# kwar(name='rahul',sname='roy')


# def kwarr(n,**kwargs):
#     print(type(kwargs))
#     for i,j in kwargs.items():
#         print(f'{i}:{j}')
# kwarr(34,name='rahul',sname='roy')
    

# da = {'name':'ram','sname':'suryawanshi'}
# kwar(**da)

######################################################**********------PADK-------***********###################################################
#MISCELLANEOUS

def fn(l,**kwargs):
    if(kwargs.get('reverse_str')):
        ll = [name[::-1].title() for name in l]
    else:
        ll = [name.title() for name in l]
    return ll

l= ['harshit','mohit']
print(fn(l))
print(fn(l,reverse_str=True))
