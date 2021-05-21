from functools import wraps

def only_support_args(types):
    def decorator(func):
        @wraps(func)
        def wrapper_func(*args,**kwargs):
            print('wrapper ')
            if all([type(s)==types for s in args]):
                return func(*args,**kwargs)
            return 'arg type incompatible'
        return wrapper_func
    return decorator

@only_support_args(float)
def normal_func(*l):
    addition =0
    for i in l:
        addition+=i 
    return addition

print(normal_func(*[2,3,4,2]))
print(normal_func(2.4,23.1,44.1))


