##def sum1(*num):
##    sum=0
##    for i in num:
##        sum=sum+i
##    print(sum)
##
##sum1(10,20)
##sum1(10,20,30)
##sum1(10,20,30,40)

def sum1(num1,*num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)

sum1(10,20)
sum1(10,20,30)
sum1(10,20,30,40)
