# positional arguement Function
def data(name,age,city):
    return f"my name is {name}my age is {age} and i live in {city}"

#print(data('Rohit',21,'Thane'))
#print(data('Robert',20,'Thane'))

#Key word Argument function
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(age=45,city='Thane',name='ABC'))
