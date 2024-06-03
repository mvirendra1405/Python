a={'name':'ABC',0:'kuch bhi','age':78,'name':'xxxxxx'}
print(a)
print(len(a))
print(type(a))


a['age']=20
a['city']='thane'
#a['name']='Rohit'
print(a)

for i in a:
    print(f"{i}={a[i]}")

'''keys=['name','age','city']
values=['xyz',33,'thane']
data={}

for i in range(len(keys)):
    data[keys[i]]=values[i]
    print(data)'''
    
print(a.keys())
print(a.values())
print(a.items())

for k,v in a.items():
    print(k,v)




