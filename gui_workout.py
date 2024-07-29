# original=int(input("enter the first value:"))
# dup=original
# squl=dup*dup
# firstvalue=0
# while(squl>0):  
#     r=squl%10
#     firstvalue=(firstvalue*10)+r
#     squl=squl//10
#     temp=0
# while(dup>0):
#     r=dup%10
#     temp=temp+(r**3)
#     dup=dup//10
#     secondvalue=temp*temp
# if(firstvalue==secondvalue):
#     print("Amstrong Number")
# else:
#     print("not")




# first=0
# second=1
# print(first)
# print(second)
# N=int(input("upto which element:"))
# for a in range(0,N):
#     third=first+second
#     print(third)
#     first,second=second,third

# n=0
# m=1
# num=int(input("enter the number:"))
# for a in range(num):
#     c=n+m
#     print(c)
#     n,m=m,c
    
# a=01
# b=1
# n=int(input("enter the value:"))
# factorial=1
# if n<0:
#     print("factorial dose not exist for negative number")
# elif n==0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         factorial=factorial*i
#         print("the factorial of ",n,"is",factorial)



# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return(x*fact(x-1))
# num=1
# print("the factorial of",num,"is",fact(num))


# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# def mod(a,b):
#     print(a%b)
# c=1
# while(c==1):
#     n=int(input("Enter Your choice 1.Add\n2.sub\n3.mul\n4.div\n5.mod "))
#     a=int(input("Enter the First value : "))
#     b=int(input("Enter the second value : "))
#     if(n==1):
#         add(a,b)
#     elif(n==2):
#         sub(a,b)
#     elif(n==3):
#         mul(a,b)
#     elif(n==4):
#         div(a,b)
#     elif(n==5):
#         mod(a,b)
#     else:
#         print("Enter the correct input!!!!!!!!!!!!!!!!!")
#     c=int(input("If you want continue , Please enter 1 ? "))
    
# def fact(n):
#     if n<2:
#         return 1
#     else:
#         return n*fact(n-1)

# def palindrome():
#     b=str(input("enter the stirng:"))
#     if b==b[::-1]:
#         print("palindorme")
#     else:
#         print("not")

# def fibo():
#     a=int(input("enter the value:"))
#     f=0
#     n=1
#     while(a>0):
#         c=f+n
#         f=n
#         n=c
#         a-=1
#         print(c)
# def adam():
#     dup=a 
#     squ1=dup*dup
#     firstvalue=0
#     while(squ1>0):
#        r=squ1%10
#        firstvalue=(firstvalue*10)+r
#        squ1=squ1//10
#     temp=0
#     while(dup>0):
#        r=dup%10
#        temp=(temp*10)+r
#        dup=dup//10
#        secondvalue=temp*temp
#        print(temp)
# def amstrong():   
#     dup=a 
#     squ1=dup*dup
#     firstvalue=0
#     while(squ1>0):
#        r=squ1%10
#        firstvalue=(firstvalue*10)+r
#        squ1=squ1//10
#     temp=0
#     while(dup>0):
#        r=dup%10
#        temp=temp+(r**3)
#        dup=dup//10
#        secondvalue=temp*temp
#        print(temp)
    
# m=int(input("Enter Your choice\n1.palindrome string\n2.fibo\n3.adam\n4.amstrong\n5.fact\npalindrome integer"))
# a=int(input("Enter the value: "))
# if(m==1):
#     print(palindrome())
# elif(m==2):
#     print(fibo())
# elif(m==3):
#     print(adam())
# elif(m==4):
#     print(amstrong())
# elif(m==5):
#     print(fact(a))
# else:
#     print("its not")



# a=str(input("enter the stirng:"))
# if a[2]=="a":
#     print(a)
# a=int(input("enter the number:"))
# if a%2==0:
#     print("add")
# else:
#     print("odd")



# b=input("enter the name:")
# if b=="monika":
#     a=(b[2:5].upper())
#     print(a)
#     print(a[:1],a[1:2],a[2:3],sep="***")
# else:
#     print("unknown")

# n=2
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")
# x=[67,45,34,23]
# sum=1
# for i in x:
#     sum=sum+i
#     print("the value:",sum)


# a=[1,2,3]
# b=a.copy()
# b.sort()
# if(a==b):
#     data=map(lambda x:x*5,a)
#     print(list(data))
# else:
#     print("no")


# a=int(input("enter the value:"))
# for i in range(4,a+1):
# #     print("*")
# for i in range(0,5):


# x="monika"
# for i in range(7):
#     print(x[:i])


# for i in range(5): 
#     print()
#     for j in range(i):
#         print(j,end="")

# for i in range(5):
#     x='*'
#     x=x*i
#     print(f"{x:^10}")

# for i in range(5):
#     x='*'
#     x=x*(5-i)
#     print(f'{x:^10}')

# for i in range(5):
#     x='*'
#     x=x*i
#     print(f"{x:>10}")

# m=input("enter the string:")
# if m=="monika":
#     for x in range(7):
#         print(m[x:])
# else:
#     print("not")

# x="*"
# for i in range(8): 
#     print()
# for j in range(i):
#     print("*",end="")


# for i in range(5): 
#     print()
#     for j in range(i):
#         print(j,end="")


###student marksheet list


# name=input("enter the name:\t")
# age=int(input("enter the age:\t"))
# fathername=input("enter the father name\t:")
# phono=int(input("enter the pho no:\t"))
# emailid=str(input("enter the email id:\t"))
# m1=int(input("enter the m1:"))
# m2=int(input("enter the m2:"))
# m3=int(input("enter the m3:"))
# m4=int(input("enter the m4:"))
# m5=int(input("enter the m5:"))
# total=m1+m2+m3+m4+m5
# print(total)
# if age>20:
#     print("your are eligiable")
# elif total>35:
#     print("pass")
# else:
#     print("fail")
# file=open("student details.txt","a")
# file.write(name)
# file.write("\t")
# file.write(str(age))
# file.write("\t")
# file.write(fathername)
# file.write("\t")
# file.write(str(phono))
# file.write("\t")
# file.write(str(emailid))
# file.write("\t")
# file.write(str(m1))
# file.write("\t")
# file.write(str(m2))
# file.write("\t")
# file.write(str(m3))
# file.write("\t")
# file.write(str(m4))
# file.write("\t")
# file.write(str(m5))
# file.write("\t")
# file.close()

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the thrid number:"))
# if(a%b%c%2==0):
#     print(a+b+c)
#     print(a/b/c)
# elif(a%2==0)and(b%2==0)or(c%2!=0):
#     print(a-b-c)
# elif(a%2==0)and(b%2!=0)or(c%2!=0):
#     print(a*b*c)
# else:
#     print("not")


# def check(d):
#     if(d%2==0):
#         return 1
#     else:
#         return 0
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# c=int(input("enter the value:"))
# i=check(a)+check(b)+check(c)
# if(i==0):
#     print(a+b+c)
# elif(i==1):
#     print(a-b-c)
# elif(i==2):
#     print(a*b*c)
# elif(i==3):
#     print(a/b/c)
# else:
#     print("not")

# import random
# a=random.randint(0,100)
# while(True):
#      b=int(input("enter the value:"))
#      if(a==b):
#        print("correct")
#        break
#      elif(a>b):
#        print("greater than")
#      elif(a<b):
#        print("less than")
#      else:
#        print("another")


