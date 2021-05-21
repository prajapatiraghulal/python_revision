# '''while and for loop '''
# #while loop

# x= input('enter your number ')
# i=0
# count=0
# while(i<len(x)):
#     count+=int(x[i])
#     i+=1
# print('sum is :',count)


# # unique letter count in name 
# z=dict()
# n = input('enter your name: ')
# i=0
# while(i<len(n)):
#     if n[i] not in z:
#         z[n[i]] =1
#     else:
#         z[n[i]]+=1
#     i+=1
# print(z)

# #for loop
# for i in range(1,21,2):
#     if(i>15):
#         break
#     if(i==13):
#         continue
#     print(i)

#     # guessing game 
    

# import random
# number = random.randint(1,100)
# attempt=0
# while True:
#     x = int(input("guess: "))
#     if x<number:
#         print("low")
#     elif x>number:
#         print('high')
#     else:
#         print(f'won the game in {attempt} attempts')
#         break
#     attempt+=1

# for i in 'raghulal':
#     print(i)

