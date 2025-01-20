
#syntax 
'''def name_of_function(arg1,arg2 ....):
       logic for function
       return 

we can use yield instead of return when we need to perform more tasks in one function, return will terminate function once code reaches return. the code defined under return will not be executed.
return is treated as last step of function.
'''

def add(a,b):
    return a+b


def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a%b

#calling the function

print(add(5,7))
print(sub(10,3))
print(mul(7,6))
print(div(6,3))

