'''generator function is alternative of list if we want some sequence of data at once without requering to store , it requere lesser memory and less 
time to create once  it returns iterator'''

import time

# def generate(n):
#     '''func to yield (generate) n number series from one'''
#     for i in range(1,n+1):
#         yield(i)

# iterate = generate(10)
# # print(next(iterate))
# # print(next(iterate))
# for i in iterate:
#     print(i, end=' ')

# print()
# count = (x**2 for x in range(10))  # similar to list comprehension generator works only difference is bracket there [] here ()
# for i in count:
#     print(i, end=' ')

t1=time.time()
lst = [i**3 for i in range(10000000)]
t_diff_1 = time.time()-t1
print(t_diff_1)
t2 = time.time()
gen = (i**3 for i in range(10000000))
t_diff_2= time.time()-t2
print(t_diff_2)

t3= time.time()
ll = list(gen)
t_diff_3 = time.time()-t3
print(t_diff_3)
