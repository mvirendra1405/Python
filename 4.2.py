#print(ord('a'))
row=97
while row<=101:
    col=97
    while col<=row:
        print(chr(row),end=" ")
        col=col+1
    row+=1
    print()
        
            
