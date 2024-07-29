
# #file handling
# #openfile #r-read operation
# file=open("new.txt","r")
# for each in file:
#     print(each)

# #method2
# file=open("word.txt","r")
# print(file.read())

# #method
# #with statement
# with open("new.txt") as file:
#     data=file.read()
# print(data)

# #read count letters
# file=open("new.txt","r")
# print(file.read(14))

# #create new file
# file=open("new.txt","w")
# file.write("\nemp name\tage\tsalary\tqualifi")
# file.write("\nanbu\t23\t2000\tdme")
# file.write("\nakash\t21\t3000\tb.sc")
# file.write("\nbijorn\t24\t4000\tdme")
# file.write("\nvishwa\t20\t1000\tdme")
# file.write("\najay\t21\t1200\tb.com")
# file.close()

# file=open("new.txt","w")
# file.write("hii")
# file.close()

# #write with new file
# file=open("new.txt","w")

# #append
# file=open("new.txt","a")
# file.write("This will add this line")
# file.close()
# myfile=open("bhavyafile.txt","r")
# myfile=open("bhavyafile.txt","r")

# #write file
# file=open("new.txt","w")
# l=["This is delhi\n","This is paris\n","This is london"]
# file.writelines(l)
# file.close()

# #append file
# file1=open("bhavyafile.txt","a")
# file1.write("hii kirthika\n")
# file1.close()

# #run on output view
# file1=open("bhavyafile.txt","r")
# print("output of readlines after appending")
# print("please enter your data:","r")
# print("please enter your data:","a")
# print(file1.read())
# print()
# file1.close()

# a=["This is Delhi \n","This is paris \n","This is london\n"] with open("bhavyafile.txt","w") as file1:
# file1.write("The statement of the view... with alone be the best")
# file1.writelines(a)

# #with open file
# with open("bhavyafile.txt","a")as file1:
#     file1.write("Today")
# with open("bhavyafile.txt","r")as file1:
#     print(file1.read())

# #file open
# file=open("test.txt","w")
# file.write("Hello World")
# file.seek(0)
# data=file.read()
# print(data)
# file.close()

# #example
# name=open("data.txt","a")
# name.write("The data are stored to content\n")
# name.write("employee name\tsalary\tdesignationaddress\t\n")
# name.write("Muruga\t\t\t10000\tBE\tmyd\n")
# name.write("Livewire\t3000\tno\tmyd\t")
# name.close()
# name=open("data.txt","r")
# print(name.read(12))
# with open("data.txt")as name:
#     data=name.read()
# print(data)



# #Delete
# import os
# if os.path.exists("new.py"):
#     os.remove("new.py")
#     print("File deleted")
# else:
#     print("File doesnot deleted")











# data=open("set.txt","w")
# data.write("emp_name\t emp_age \t emp_country \t emp_mailid\n")
# data.write("kannan   \t     23  \t mayalsia  \t kannan@gamil.com\n")
# data.close()



# data=open("set.txt","r")
# print(data.read())



# import os
# if os.path.exists("we.py"):
#     os.remove("we.py")
#     print("file deleted")
# else:
#     print("file doesnot deleted")



#file handling




# name=open("type.txt","w")
# name.write("the data are the stored in the many value of the file handling content\n")
# name.write("name   \t subject  \t  class   \t  country\n")
# name.write("monika \t computer  \t  m.sc   \t  tamil nadu\n")
# name.write("the content of the many string value")
# name.close()
# name=open("type.txt","r")
# print(name.read(10))
# name=open("type.txt","w")
# S={"this is delhi \n","this is paris \n","this is london\n"}
# name.writelines(S)
# name.close()
          
# name=open("type.txt","w")
# print("the number of the value")
# print("please enter a value number:")
# print("please enter a value number:")
# print(name.read())
# name.close()



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
