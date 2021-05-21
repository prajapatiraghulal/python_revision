# # # l = [1,2,'ram',2.34,'ramesh']
# # # print(l[0:-1:1])
# # # l[1:]= ['ek']
# # # print(l)

# # #print(dir(list))
# l=[1,2,3]

# # # p = l
# # # p[0]=323
# # # print(l)
# # print(l)
# # q=l.copy()
# # q[0]=1000
# # print(l)
# # print(q)
# # l.append(34)
# # print(l)
# # l.insert(1,'raja')
# # print(l)
# q=['raja','rama','mohan']
# # t = q+l
# # print(t)

# #q.extend(l)
# #print(q)

# # x=q.pop()
# # print(q,x)
# # y =q.pop(1)
# # print(y,q)

# # del q[0]
# # print(q)
# # q.remove('raja')
# # print(q)


# # if 'rama' in q:
# #     print("found")
# # else :
# #     print("not found")

# # print(q.count('rama'))
# # #q.sort()
# # #print(q)
# # print(sorted(q),q)
# # # q.clear()
# # # print(q)
# # n = q.copy()
# # n[0]=32
# # print(n,q)

# # temp = [3,2,5,2]
# # te = [3,2,5,2]
# # tb = temp
# # tc= temp.copy()
# # tt=[2,3,2,5]
# # print(temp==tt)
# # print(temp == te)

# # print(temp is te)
# # print(temp is tb)
# # print(temp is tc)

# # string = "ramesh 34 mahesh"
# # lst = string.split()
# # print(lst)
# # temp = ' '.join(lst)
# # print(temp)
# # print(type(temp))

# # print(type(range(10)))

# lst = list(range(10))
# # lst.append(1)
# # lst.append(8)
# # print(lst)
# # print(lst.index(1))
# # print(lst.index(1,2))
# # print(lst.index(1,2,11))   #search for first 1 bw 2-11(ex) 

# # def lst_change(l):
# #     l[0]=89

# # lst_change(lst)
# # print(lst)

# # def fn(l):
# #     even=[]
# #     odd=[]
# #     for i in l:
# #         if(i%2==0):
# #             even.append(i)
# #         else:
# #             odd.append(i)
# #     return [even,odd]

# # print(fn(lst))
        
# # print(min(lst))
# # print(max(lst))

# tt = [3,2,[32,2],2,[32],0,[34]]
# # print(type(tt[2]))
# # print(type(list))
# def lst_check(ttd):
#     count=0
#     for i in ttd:
#         if (type(i)==type([])): # type([]) is similar to list
#             count+=1
#     return count
# print(lst_check(tt))    

# #print(type(tt[2])==type([]))


ll= [3,4,'ram']
x,y,z = ll
print(x,y,z)