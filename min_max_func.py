'''takes argument and return min or max based on key=func param'''

# la = [1,34,-130,2,0,100]
# lb = [1,2,3,4,55,100]
# print(min(la), max(la))

# print(max(la, key=lambda s: s if s>=0 else -s))

students = {
    'harshit' : {'score':90, 'age':24},
    'mohit':{'score':75, 'age':19},
    'rohit':{'score':76, 'age':23}
}
print(students)
print(max(students,key=lambda s:students[s]['score']))