# x=8
# def change():
#     x=100
#     return(x)
# print(x)
# print(change())

x=8
def change():
    global x
    x=100
    return(x)
print(x)
print(change())
print(x)

