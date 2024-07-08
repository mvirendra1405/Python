'''Class is a blueprint that defines some properties and behaviours.An object is an instance of
   a class that has those properties and behaviours attached .A class is not allocated memory
   when it is defined.An object is allocated memory when it is created.class is a logical entity
   whereas object are physical entities.'''
##a=10
##print(type(a))
##
##b=20
##print(type(b))

##b='rajesh'
##print(type(c))
##
##class str
##
##class student

##class student:
##    name='Virendra'
##    email='v@gamail.com'
##    roll_no=14
##
##s=student
##print(s.name)
##print(s.email)
##print(s.roll_no)

##class student:
##    name='virendra'
##    email='v@gmail.com'
##    roll_no=14
##
##    def demo(s):
##        name='virendra'
##        print(name)
##
##s=student()
##s.demo()

##class student:
##    name='virendra'
##    email='v@gmail.com'
##    roll_no=14
##
##    def demo(self):                 #Self is default parameter that represents instance of class
##        name='virendra'
##        print(name)
##
##s=student()
###s.demo()
##k=student()
##k.demo()
##
##m=student()
##m.demo()

##class A:
##    def demo(self,department):
##        print(department)
##        print(self)
##        name='virendra'
##        age=30
##        roll_no=14
##        print(name,age,roll_no)
##
##    def display(self):
##        email='v@gmail.com'
##        address='thane'
##        print(email,address)
##
##a=A()
####a.demo()
####print(a)
####
####a.display()
####A.demo('k')
##a.demo('mech')

class student:
    def show(self,name,roll_no,dept):
        print('My name is',name)
        print('roll_no is',roll_no)
        print('dept is',dept)
        print('I am a python developer')
        

    def display(self):
        print('Java developer')

s=student()
s.show('virendra',14,'software developer')
s.display()




    

