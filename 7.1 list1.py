#creating list with constructor method

'''a=list((1,2,'abc','xyz'))
print(a)
print(type(a))
print(len(a))

b=['xyz','abc',123,44,55]
print(a)
print(type(a))
print(len(a))'''

'''a=['robert','anuj','mishraji','saud','jadhav','nair']
for i in a:
    if i[-1]=='i':
        print(i)'''

'''a=['robert','anuj','mishraji','saud','jadhav','nair']
for i in a:
    if 'r' in i:
        print(i)'''

'''a=['robert','anuj','mishraji','saud','jadhav','nair']
for i in a:
    for j in i:
        if j=='r':
            print(i)
            break'''

'''a=['robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']
i=0
while(i<len(a)):
    j=0
    while j<len(a[i]):
        if a[i][j]=='r':
            print(a[i])
            break
        j+=1
    i+=1'''

a=['robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a[i]):
        if a[i][j] in 'aeiou':
            c=c+1
        j+=1
    print(f"{a[i]}this name contains {c} vowels")
    i+=1
            
        
