'''for i in range(1,50,1):
    if i%2==0:
          print(i)'''

##for i in range(1,100,1):
##    if i%2==0:
##          print(i)

'''a=[1,2,3,4,5,6,7,8,9,10]
e=[]
o=[]

for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)'''
            
'''a=[1,2,3,4,5,6,7,7,7,6,6,6,4]
b=[]
c1=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c1.append(i)
print(b)
print(c1)
for i in b:
    c2=0
    for j in c1:
        if j==i:
            c2=c2+1
    if c2:
        print(f" {i} duplicates are {c2}")'''

'''a=[[['robert','mishraji','anuj','rajith','jadhav']]]
for i in a[0][0]:
    print(i)'''

'''a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in a:
    for j in i:
        print(j)'''
    
'''a=[[['robert','mishraji','anuj','rajith','jadhav']]]
i=0
while i<len(a[0][0]):
    print(a[0][0][i])
    i+=1'''

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1









    

