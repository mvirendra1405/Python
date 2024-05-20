n=8208
n1= n
l=len(str(n))
s=0
while n!=0:
    r = n%10
    s = s+r**l 
    n = n//10

if n1 == s:
    print("This is an Armstrong number")
else:
    print("Not a Armstrong")


