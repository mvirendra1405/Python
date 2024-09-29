'''a=(1,2,3,'abc','xyz')
print(a)
print(type(a))
print(len(a))
print(a[-1])

#a[0]="Rohit"
# print(a)

b=(1,2)
print(type(a+b))
s=(1,)
print(type(s))

data=('rohit',54,'Thane',11,222,33,55,66,77)
(name,age,city,*a)=data
print(city)
print(a)
print(a[2])'''

a=[1,2,3,([33,88,'abc',('yes','No','yes')])]
##a[3][3]=('yes','yes','yes')
##print(a)

'''b=list(a[3][3])
b[1]='yes'
print(tuple(b))
a[3][3]=tuple(b)

print(a)

a=(1,2,3,3,4,3)
print(a[::-1])
print(a.count(2))'''


n=(1,1,2,3,3,4,3)

for i in n:
    print(i)

i=0
while i<len(n):
    print(n[i])
    i+=1

for i in range(len(n)):
    print(n[i])














