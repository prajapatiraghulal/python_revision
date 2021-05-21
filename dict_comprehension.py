# da = {key:key**2 for key in range(10)}
# print(da)

# db = {f"square of {key} is ":key**2 for key in range(5)}
# print(db)
# for a,b in db.items():
#     print(f"{a}:{b}")

# dc = {key:key**2 if key%2==0 else -key for key in range(10) }
# print(dc)

s = 'maharaj'
dd = {i:s.count(i) for i in s}
print(dd)