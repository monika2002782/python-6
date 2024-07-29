#function
#basic
def myfunction():
   print("hello world")
myfunction()

#argument
def addnum(num1,num2):
   print(num1+num2)
addnum(2,3)

#return keyword
def function(name,age):
   print(name,age)
function("livewire",23)
def multiplynum(num1):
 return num1*7
result=multiplynum(8)
print(result)



#recursion
def factorial(x): 
   if x==1:
    return 1
   else:
    return (x*factorial(x-1))
num=5
print("the factorial of",num,"is",factorial(num))




'''def add(a,b):
    result=a+b
    return result
def sub(a,b):
    result=a-b
    return result
def mul(a,b):
    result=a*b
    return result
def div(a,b):
    result=a/b
    return result
'''
def greeting(name):
    print("my name is:",name)

