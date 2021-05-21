'''similar to map fn but it creates filter object which contains element with true fn(element) and that object is  only once iterable '''
fn = filter(lambda s: True if s%2==0 else False ,[1,2,3,4])
# for i in fn:
#     print(i)

la = list(fn)
print(la)

