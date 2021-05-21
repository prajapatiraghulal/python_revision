def square(num):
    return num**2

la = [1,2,3,4,5]
# ma = map(square, la)
# print(ma) 
# print(list(ma))  

#or

mb = map(lambda num: num**2, la)
lb = list(mb)
print(lb)


#map object is iterable but only once second loop will not iterate 