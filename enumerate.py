'''provides counting with looping '''
# for i,j in enumerate(range(5,10,1)):
#     print(f'{i}----->{j}')

la=['ram','mohan','sohan','raja','birbal','rani','sita']

def searching(l,name):
    for i,j in enumerate(l):
        if(j==name):
            return i

print(searching(la,'raja'))
print(searching(la,'rani'))