#Recursion:When a function call itself,then that function is called
#as recursive  function and the process is called as recursion.

##def demo():
##    print('Virendra')
##    demo()
##
##demo()
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print('Virendra',i)
##    demo()
##
##demo()

##import sys
##
##print(sys.getrecursionlimit())
##sys.setrecursionlimit(200)
##print(sys.getrecursionlimit())
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print('Virendra',i)
##    demo()
##
##demo()

##Advantage:
##1)clean code/less number of code
##2)complex problem can be solved

##Disadvantages:
##1)hard to debug
##2)not memory efficient

##WAP for fibbonacci series using recursion
##0,1,1,2,3,5,......
##
##fibo(1)=0
##fibo(2)=1
##fibo(3)=fibo(1)+fibo(2)
##fibo(3)=fibo(3-2)+fibo(3-1)
##fibo(n)=fibo(n-2)+fibo(n-1)

##def fibo(n):
##    if n==1:
##        return 0
##    if n==2:
##        return 1
##    return fibo (n-2) + fibo(n-1)
##n=int(input('Enter the number of terms: '))
##print(fibo(n))

























