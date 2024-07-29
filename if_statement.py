#if statement
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
std=int(input("enter your std:"))
school=input("enter your school:")
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
total=tamil+english+maths
average=total/3
print(total)
print(average)
if total>250:
    print("you got a bio")
else:
    print("you got a com")

#if statement
num=int(input("Enter your number: "))
if num > 0:
   print("The number is positive")
else:
    print("negative number")

# if else
age=int(input("enter your age:"))
if age<18:
    print("your are eligible to vote")
else:
    print("your are not eligible to vote")
    
#if else
age=int(input("enter your age:"))
if age>25:
    print("your are eligible to election:")
else:
    print("your are  not eligible to election:")

#workout
student=int(input("enter your number:"))
name=str(input("enter your name:"))
std=int(input("enter your std:"))
age=int(input("enter your age:"))
place=str(input("enter your place:"))
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
science=int(input("enter your science marks:"))
social=int(input("enter your social marks:"))
total=tamil+english+maths+science+social
print(total)
if (total>400)and(age>=15):
    print("the student is bio")
    print("there is a markstatement")
else:
    print("the student is com")
    print("there is not markstatement")

    #elif
num=int(input("enter your number:"))
if num>30:
     print("good")
elif num==30:
    print("this is equal")
else:
    print("bad")

#nestedif
num=int(input("enter your number:"))
if num>=0:
 if num==0:
        print("this is equal to 0")
 else:
    print("this is positive number")
else:
    print("this is negative number")

#if workout
age=int(input("enter your age:"))
if(age<30):
    print("you are eligible")
else:
    print("you are not eligible")

    #nested
username=input("enter your username:")
password=input("enter your password:")
if username=="bhavya":
  if password=="livewire":
    print("login a successful!welcome admin")
  elif password=="12345":
    print("weak password.please reset your password")
  else:
    print("incorrect password.please try again")
else:
        if username=="dd":
           if password=="jan":
             print("login successful welcome dd")
           else:
             print("incorrect password please try again")
        else:
               print("unknown user.please try again")


























'''#if statement
num=int(input("Enter your number: "))
if num > 0:
    
    print("The number is positive")

else:
    print("negative number")
'''



'''age=int(input("enter your age:"))
if age<18:
    print("your are eligible to vote")

else:
    print("your are not eligible to vote")'''
    
'''

age=int(input("enter your age:"))
if age>25:
    print("your are eligible to election:")
else:
    print("your are  not eligible to election:")


student=int(input("enter your number:"))
name=str(input("enter your name:"))
std=int(input("enter your std:"))
age=int(input("enter your age:"))
place=str(input("enter your place:"))
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
science=int(input("enter your science marks:"))
social=int(input("enter your social marks:"))
total=tamil+english+maths+science+social
print(total)
if (total>400)and(age>=15):
    print("the student is bio")
    print("there is a markstatement")
else:
    print("the student is com")
    print("there is not markstatement")

    
["apple","mango"]
b=["apple","mango"]
print(a is  b)
x=4
y=7
print((x>2)and(y>5))'''

# num=int(input("enter your number:"))
# if num>30:
#      print("good")
# elif num==30:
#     print("this is equal")
# else:
#     print("bad")

# num=int(input("enter your number:"))
# if num>=0:
#  if num==0:
#         print("this is equal to 0")
#  else:
#     print("this is positive number")
# else:
#     print("this is negative number")



# a=90
# b=89
# print(a>90)and(b<90)
# print(not(a>89 and b>78))
# age=int(input("enter your age:"))
# if(age<30):
#     print("you are eligible")
# else:
#     print("you are not eligible")




# nested if statement
# username=input("enter your username:")
# password=input("enter your password:")
# if username=="bhavya":
#   if password=="livewire":
#     print("login a successful!welcome admin")
#   elif password=="12345":
#     print("weak password.please reset your password")
#   else:
#     print("incorrect password.please try again")
# else:
#         if username=="dd":
#            if password=="jan":
#              print("login successful welcome dd")
#            else:
#              print("incorrect password please try again")
#         else:
#                print("unknown user.please try again")


###arbitary

# def myfunction(*kids):
#   print(kids[0])
# myfunction("emil","hani","linus")
# def my_function(**kid):
#   print("his last name is"+kid["fname"]+kid["lname"])
# my_function(fname="nitharshan",lname="hani")
# def my_function(country="norway"):
#   print("I am from"+country)
# my_function("sweden")
# my_function()
# my_function("india")




# a=str(input("enter the stirng:"))
# # # if a[2]=="a":
# #     print(a)
# # a=int(input("enter the number:"))
# # if a%2==0:
# #     print("add")
# # else:
# #     print("odd")



# # b=input("enter the name:")
# # if b=="monika":
# #     a=(b[2:5].upper())
# #     print(a)
# #     print(a[:1],a[1:2],a[2:3],sep="***")
# # else:
# #     print("unknown")

# # n=2
# # for i in range(2,n):
# #     if n%i==0:
# #         print("not prime")
# #         break
# #     else:
# #         print("prime")
# # x=[67,45,34,23]
# # sum=1
# # for i in x:
# #     sum=sum+i
# #     print("the value:",sum)


# # a=[1,2,3]
# # b=a.copy()
# # b.sort()
# # if(a==b):
# #     data=map(lambda x:x*5,a)
# #     print(list(data))
# # else:
# #     print("no")
