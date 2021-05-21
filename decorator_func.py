'''decorator is a way to increase functionality of functions '''
from functools import wraps
import functools
import time

# def decorator_func(function):
#     print('this is decorator_func')
#     @wraps(function)
#     def wrapper_func(*args,**kwargs):
#         '''hello wrapper doc'''
#         print('this is wrapper func')
#         return function(*args,**kwargs)
#     return wrapper_func





# @decorator_func
# def add(a,b):
#     '''doc this is add takes 2 args and return 1 sum'''
#     print(f'{a},{b},{a+b}')
#     return(a,b)

# # da = decorator_func(add)
# # print('#################')
# # print(da(2,2))
# # print(add.__doc__,'\n',add.__name__)

# print(add(2,3))
# print(add.__name__, add.__doc__)

# print(dir(functools))

def calculate_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        # x= func(*args,**kwargs)
        # t2= time.time()
        # return x,t2-t1
        return func(*args,**kwargs),time.time()-t1    #this way takes bit longer time

    return wrapper

@calculate_time
def func(a,b):
    '''func takes two args and return a string'''
    j=0
    for i in range(1000000):
        j+=1
    return f'func {a},{b} : '

print(func(3,2))



