name = 'rawan ji'

if len(name)>=5:
    print(f'your name is {name} ')
elif len(name)<=2:
    print(f'very short name')
else:
    print(f'short name ')


n = input('enter your name:')
if name:
    print(f"your name is {name}")
else:
    print(f'no input')


#use of in
if 'r' in n:
    print(f'lucky name')
