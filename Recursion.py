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

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())

i=0
def demo():
    global i
    i=i+1
    print('Virendra',i)
    demo()

demo()












