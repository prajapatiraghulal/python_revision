st= 'papMepswaR'
print(st[4])
print(st[-2])
print(st[2:4])
print(st[2:-4]) 
print(st[0:6:2])  #step of 2
print(st[-1:0:-1])

#print(dir(str))
print(len(st))
print(st.upper())
print(st.lower())
print(st.title())
print(st.upper().count('R'))


x = '    raja ki rani.  '
print(x.strip()+'check')
print(x.rstrip()+'check')
print(x.lstrip()+'check')


print(st.replace('p','P',2))
print(st)

#print(help(str.find))
print(x.find('i'))
print(x.find('i',x.find('i')+1))

print(x.center(len(x)+4, "#"))

