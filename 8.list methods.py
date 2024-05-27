a=[1,2,3,'abc','xyz']
a.append("Added")
print(a)

a=[1,2]
b=[3,4]
a.extend(b)
b.extend(a)
print(b)

a=[1,2,3,4]
a.insert(0,100)
a.insert(0,100)
a.insert(2,300)
a.insert(2,400)
print(a)

a=['abc',100,200]
a[1]='robert'
print(a)

a=[1,2,3,4,'abc','yyyyy',4]
a.pop()
a.remove('abc')
print(a)

a=[1,2,3,4,4]
del a[0]
print(a)

ab=[1,2,3,3,3]
print(ab.count(3))

print(ab.index(3))
