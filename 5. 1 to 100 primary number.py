for n in range(1,101,1):
    for j in range(2,n,1):
        if n%j==0:
            break
    else:
        print(n)
