#class creation
'''class myclass():
    x=5
print(myclass)'''



#class and object
'''class addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("first number="+str(self.first))
        print("second number="+str(self.second))
        print("addition of two numbers="+str(self.answer))
    def calculate(self):
        self.answer=self.first+self.second
obj1=addition(100,200)
obj2=addition(20,20)
obj1.calculate()
obj2.calculate()
obj1.display()
obj2.display()'''

#class workout
'''class students():
    def __init__(self,mark,result):
        self.mark=mark
        self.result=result
    def demo(self):
        print("total marks is: ",self.mark)
        print("Result: ",self.result)
obj1=students(78,230)
obj2=students(90,250)
obj3=students(40,590)
obj1.demo()
obj2.demo()
obj3.demo()   ''' 

#class workout
'''class student:
    def __init__(self):
        name="keerthi"
        age=89
        salary=6000
        designation="developer"
        print("name:",name)
        print("age:",age)
        print("salary:",salary)
        print("designation:",designation)
        std=student()'''

#class work
'''class person:
    def __init__(self):
        print("1")
    def __init__(self):
        print("2")
p1=person()
p2=person()'''



# var="apple"
# myiter=iter(var)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# def var():
#     n=1
#     while n<10:
#         val=n*n
#         yield val
#         n+=1
# a=var()
# for i in a:
#     print(i)   
