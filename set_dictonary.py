a = [1,1,1,1,2,3,1,2,3,2,1,3]
b = {}
for i in a:
    if i in b.keys():
        b[i] +=1
    else:
        b[i] = 1    
print(b)

c = {"name":"mamun","age":23}
for k,v in c.items():
    print(f"{k}:{v}")
