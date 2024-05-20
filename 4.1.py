row=1
while row<=5:
    col=1
    while col<=5:
        if row==1:
            print("A",end=" ")
        elif col==1:
            print("C",end=" ")
        elif row==col:
            print("B",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    row=row+1
    print()
