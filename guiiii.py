
# from tkinter import *
# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()   



##Text
# from tkinter import *
# from tkinter import Tk
# root = Tk()
# text = Text(root,height=2, width=30)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
# b=Button(root,text="submit")
# b.pack()
# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="orange", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
# root.mainloop()     
    


# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
# mainloop()




# from tkinter import*
# root=Tk()
# root.title("Registraction From")
# root.geometry("50x50")
# l=Label(root,text="Registraction From",width=20,bg="violet",fg="blue",font=("bold",10)).grid(row=0,column=1)
# l2=Label(root,text="Name",width=20,bg="orange",fg="green",font=("bold",5)).grid(row=1,column=1)
# e1=Entry(root)
# e1.grid(row=0,column=2)
# l3=Label(root,text="Age",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=1,column=1)
# e2=Entry(root)
# e2.grid(row=1,column=2)
# l4=Label(root,text="DOB",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=2,column=1)
# e3=Entry(root)
# e3.grid(row=2,column=2)
# l5=Label(root,text="Phone no",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=3,column=1)
# e4=Entry(root)
# e4.grid(row=3,column=2)
# l6=Label(root,text="Email id",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=4,column=1)
# e5=Entry(root)
# e5.grid(row=4,column=2)
# l7=Label(root,text="Gender",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=5,column=1)
# e6=Entry(root)
# e6.grid(row=5,column=2)
# l7=Label(root,text="Aadhar no",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=6,column=1)
# e7=Entry(root)
# e7.grid(row=6,column=2)
# l8=Label(root,text="Address",width=10,bg="orange",fg="green",font=("bold",5)).grid(row=7,column=1)
# e8=Entry(root)
# e8.grid(row=7,column=2)
# def data():
#     a=e1.get()
#     b=e1.get()
#     c=e1.get()
#     d=e1.get()
#     e=e1.get()
#     f1=e1.get()
#     h=e1.get()
#     i=e1.get()
#     f=open("set.txt","a")
#     f.write(a+" "+b+" "+c+" "+d+" "+e+" "+f1+" "+h+" "+i)
# but=Button(root,text="Click",width=20,bg="pink",fg="blue",font=("bold",5),command=data).grid(row=8,column=2)
# root.mainloop()


# # from tkinter import *


# def sel():
#     selection = "You selected the option " + str(var.get())
#     label.config(text=selection)

# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
#                  command=sel)
# R1.pack(anchor=W)
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                  command=sel)
# R2.pack(anchor=W)
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                  command=sel)
# R3.pack(anchor=W)

# label = Label(root)
# label.pack()
# root.mainloop()

# from tkinter import *
# from tkinter import messagebox

# root=Tk()

# l1=Label(root,text="Name")
# l1.grid(row=0,column=1)
# l2=Label(root,text="Father Name")
# l2.grid(row=1,column=1)
# l3=Label(root,text="Age")
# l3.grid(row=2,column=1)
# l4=Label(root,text="Degree")
# l4.grid(row=3,column=1)
# l5=Label(root,text="Address")
# l5.grid(row=4,column=1)
# text=Text(root,height=3,width=30)
# text.grid(row=4,column=2)
# l6=Label(root,text="Gender")
# l6.grid(row=5,column=1)
# l7=Label(root,text="Physically Challenged Person")
# l7.grid(row=6,column=1)
# l8=Label(root,text="Sports Quota")
# l8.grid(row=7,column=1)

# e1=Entry(root)
# e1.grid(row=0,column=2)
# e2=Entry(root)
# e2.grid(row=1,column=2)
# e3=Entry(root)
# e3.grid(row=2,column=2)

# checkbox1=IntVar()
# checkbox2=IntVar()
# checkbox3=IntVar()


# c1=Checkbutton(root,text="UG",variable=checkbox1,onvalue=1,offvalue=0,height=1,width=10)
# c1.grid(row=3,column=2)
# c2=Checkbutton(root,text="PG",variable=checkbox2,onvalue=1,offvalue=0,height=1,width=10)
# c2.grid(row=3,column=3)
# c3=Checkbutton(root,text="other",variable=checkbox3,onvalue=1,offvalue=0,height=1,width=10)
# c3.grid(row=3,column=4)


# var=IntVar()
# var1=IntVar()
# var2=IntVar()
# r1=Radiobutton(root,text="Male",variable=var,value=1)
# r1.grid(row=5,column=2)
# r2=Radiobutton(root,text="Female",variable=var1,value=2)
# r2.grid(row=5,column=3)
# r3=Radiobutton(root,text="Transgender",variable=var2,value=3)
# r3.grid(row=5,column=4)

# var4=IntVar()
# var5=IntVar()
# r1=Radiobutton(root,text="Yes",variable=var4,value=1)
# r1.grid(row=6,column=2)
# r2=Radiobutton(root,text="No",variable=var5,value=2)
# r2.grid(row=6,column=3)
# var6=IntVar()
# var7=IntVar()

# r1=Radiobutton(root,text="Yes",variable=var6,value=1)
# r1.grid(row=7,column=2)
# r2=Radiobutton(root,text="No",variable=var7,value=2)
# r2.grid(row=7,column=3)


# def name():
#     a=e1.get()
#     b=e2.get()
#     c=e3.get()
#     h=open("std detail.txt","a")
#     h.write("\n"+a+" "+b+" "+c)
#     gen=""
#     if(var==1):
#         print("male")
#     elif(var1==2):
#         print("female")
#     else:
#         print("transgender")



# button=Button(root,text="register",command=name)
# button.grid(row=8,column=0)

# root.mainloop()


# import tkinter
# top=tkinter.Tk()
# top.mainloop()



# from tkinter import*
# name=Tk()
# frame=Frame(name,bg="violet",width=80,height=70)
# frame.pack()
# name.mainloop()



# from tkinter import*
# high=Tk()
# f=Frame(high,bg="green",width=60,height=68)
# b=Button(high,bg="yellow",width=10,height=10)
# b.pack()
# f.pack()
# high.mainloop()



# from tkinter import*
# name=Tk()
# f1=Frame(name)
# f2=Frame(name)
# l=Label(f1,text="Hi monika",bg="violet")
# l.pack()
# b=Button(f2,text="welcome",bg="green")
# b.pack()
# f1.pack(padx=50,pady=70)
# f2.pack(padx=70,pady=40)
# name.mainloop()



# from tkinter import*
# name=Tk()
# f1=Frame(name)
# f2=Frame(name)
# for i in["blue","red","violet","pink","white","black"]:
#     Frame(name,height=10,width=20,bg=i).pack()
#     f1.pack(padx=50,pady=70)
#     f2.pack(padx=70,pady=40)
# name.mainloop()



# from tkinter import*
# hide=Tk()
# hide.mainloop()
# from tkinter import*
# name=Tk()
# name.title("welcome to my channel")
# name.mainloop()



# from tkinter import*
# root=Tk()
# root.title("welcome to geek for geek")
# root.geometry("350x350")
# lbl=Label(root,text="the main postion")
# lbl.grid()
# def clicked():
#     lbl.configure(text="the liked")
# b=Button(root,text="click me",fg="red",command=clicked)
# b.grid(column=1,row=0)
# root.mainloop()



# from tkinter import*
# root=Tk()
# root.title("welcome our channel")
# L=Label(root,text="the main position")
# L.grid()
# root.geometry("400x600")
# root.mainloop()



# from tkinter import*
# root=Tk()
# root.title("welcome to geekfoprgeeks")
# root.geometry("350x450")
# lbl=Label(root,text="are you there")
# lbl.grid()
# txt=Entry(root,width=10)
# txt.grid(column=1,row=0)
# def clicked():
#     lbl.configure(text="this is the main portion")
# btn=Button(root,text="click me",fg="red",command=clicked)
# btn.grid(column=2,row=0)
# root.mainloop()





# from tkinter import*
# root=Tk()
# w=Canvas(root,width=40,height=50)
# w.pack()
# Canvas_height=20
# Canvas_width=200
# y=int(Canvas_height/2)
# w.create_line(0,y,Canvas_width,y)
# root.mainloop()




# from tkinter import*
# root=Tk()
# var1=IntVar()
# Checkbutton(root,text="male",variable=var1).grid(row=0,sticky=W)
# var2=IntVar()
# Checkbutton(root,text="female",variable=var2).grid(row=1,sticky=W)
# root.mainloop()



# from tkinter import*
# root=Tk()
# Label(root,text="First name").grid(row=0)
# Label(root,text="last name").grid(row=1)
# e1=Entry(root)
# e2=Entry(root)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# root.mainloop()





# from tkinter import*
# root=Tk()
# frame=Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side=BOTTOM)
# btn=Button(frame,text="violet",fg="violet")
# btn.pack(side=LEFT)
# btn2=Button(frame,text="brown",fg="green")
# btn2.pack(side=RIGHT)
# btn3=Button(frame,text="yellow",fg="yellow")
# btn3.pack(side=LEFT)
# root.mainloop()





# from tkinter import*
# top=Tk()
# nm=Listbox(top)
# nm.insert(1,"python")
# nm.insert(2,"c++")
# nm.insert(3,"c")
# nm.insert(4,"php")
# nm.insert(5,"anyother")
# nm.pack()
# top.mainloop()



# from tkinter import*
# root=Tk()
# menu=Menu(root)
# root.config(menu=menu)
# filemenu=Menu(menu)
# menu.add_cascade(label="File",menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='file')
# filemenu.add_command(label='open')
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=root.quit)
# helpmenu=Menu(menu)
# menu.add_cascade(label="Help",menu=helpmenu)
# helpmenu.add_command(label='About')
# root.mainloop()




# from tkinter import*
# root=Tk()
# menu=Menu(root)
# root.config(menu=menu)
# filemenu=Menu(menu)
# menu.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open...")
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu=Menu(menu)
# menu.add_cascade(label="help",menu=helpmenu)
# helpmenu.add_command(label="About")
# root.mainloop()





# from tkinter import*
# root=Tk()
# ourMessage="this is a our message"
# msg=Message(root,text=ourMessage)
# msg.config(bg="lightgreen")
# msg.pack()
# root.mainloop()




# from tkinter import*
# root=Tk()
# v=IntVar()
# Radiobutton(root,text="GFG",variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text="MIT",variable=v,value=2).pack(anchor=W)
# root.mainloop()
# from tkinter import*
# root=Tk()
# w=Scale(root,from_=0,to=50)
# w.pack()
# w=Scale(root,from_=0,to=400,orient=HORIZONTAL)
# w.pack()
# root.mainloop()



# from tkinter import*
# root=Tk()
# Scrollbar=Scrollbar(root)
# Scrollbar.pack(side=RIGHT,fill=Y)
# m=Listbox(root,yscrollcommand=Scrollbar.set)
# for line in range(100):
#     m.insert(END,"livewire"+str(line))
# m.pack(side=LEFT,fill=BOTH)
# Scrollbar.config(command=m.yview)
# root.mainloop() 



# from tkinter import*
# root=Tk()
# t=Text(root,height=4,width=30)
# t.pack()
# t.insert(END,"the begend a seasons\nin  the world of python")
# t.config(bg="violet")
# root.mainloop()



# from tkinter import*
# root=Tk()
# root.title("moni")
# t=Toplevel()
# t.title("python")
# root.mainloop()




# from tkinter import*
# r=Tk()
# w=Spinbox(r,from_=0,to=80)
# w.pack()
# w.config(bg="red")
# r.mainloop()



# from tkinter import*
# from PIL import ImageTk,Image
# from PIL.ImageTk import PhotoImage
# r=Tk()
# r.geometry("500x800")
# frame=Frame(r,width=600,height=400)
# frame.pack()
# frame2=Frame(r,width=500,height=400)
# frame2.pack()
# frame.place(anchor="center",relx=0.5,rely=0.5)
# frame2.place(anchor="w",relx=0.8,rely=0.8)
# img2=PhotoImage(Image.open("php.jpg"))
# img=PhotoImage(Image.open("py.jpg"))
# lbl=Button(frame,image=img)
# lbl2=Button(frame,image=img2)
# lbl.pack()
# lbl2.pack()
# r.mainloop()





# import tkinter as tk
# root=tk.Tk()
# root.geometry("600x400")
# name_var=tk.StringVar()
# paswd_var=tk.StringVar()
# def submit():
#     name=name_var.get()
#     password=paswd_var.get()
#     print("the name is :"+name)
#     print("the password is:"+password)
# name_var.set("")
# paswd_var.set("")
# name_lbl=tk.Label(root,text="username",font=("calibre",10,"bold"))
# name_ery=tk.Entry(root,textvariable=name_var,font=("calibre",10,"normal"))
# password_lbl=tk.Label(root,text="password",font=("calibre",10,"bold"))
# password_ery=tk.Entry(root,textvariable=paswd_var,font=("calibre",10,"normal"),show="*")
# sub_btn=tk.Button(root,text="submit",command=submit)
# name_lbl.grid(row=0,column=0)
# name_ery.grid(row=0,column=1)
# password_lbl.grid(row=1,column=0)
# password_ery.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)
# root.mainloop()






# from tkinter import *
# r=Tk()
# r.geometry("400x400")

# l1=Label(r,text="Enter the First Value")
# l1.grid(row=0,column=1)
# l2=Label(r,text="Enter the Second Value")
# l2.grid(row=1,column=1)
# l3=Label(r,text="Result")
# l3.grid(row=2,column=1)

# e1=Entry(r)
# e1.grid(row=0,column=2)
# e2=Entry(r)
# e2.grid(row=1,column=2)
# e3=Entry(r)
# e3.grid(row=2,column=2)

# def add():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a+b
#     e3.delete(0,END)   
#     e3.insert(0,c)
# b=Button(r,text="add",command=add)
# b.grid(row=5,column=2)
# def mul():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a*b
#     e3.delete(0,END)  
#     e3.insert(0,c)
# b2=Button(r,text="mul",command=mul)
# b2.grid(row=6,column=2)
# def div():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a/b
#     e3.delete(0,END)  
#     e3.insert(0,c)
# b3=Button(r,text="div",command=div)
# b3.grid(row=7,column=2)
# def sub():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a-b
#     e3.delete(0,END)  
#     e3.insert(0,c)
# b4=Button(r,text="sub",command=sub)
# b4.grid(row=8,column=2)
# r.mainloop()



# from tkinter import*
# r=Tk()
# r.title("register form")
# r.geometry("450x450")
# lbl=Label(r,text="REGISTRATION FORM",fg="black",font=20)
# lbl.place(anchor="s",x=90,y=120)
# r.mainloop()



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



####Registration form

# from tkinter import*
# root=Tk()
# root.title("Registration Form")
# root.geometry("400x600")
# lbl=Label(root,text="Registration Form",width=20,font=("bold",22))
# lbl.place(relx=0.1,rely=0.1)
# lbl2=Label(root,text="Name",width=20,font=("arial",10))
# lbl2.place(relx=0.1,rely=0.2)
# entry1=Entry(root)
# entry1.place(relx=0.2,rely=0.2)
# lbl3=Label(root,text="Age",width=20,font=("bold",10))
# lbl3.place(relx=0.1,rely=0.3)
# entry2=Entry(root)
# entry2.place(relx=0.2,rely=0.3)
# lbl4=Label(root,text="DOB",width=20,font=("bold",10))
# lbl4.place(relx=0.1,rely=0.4)
# entry3=Entry(root)
# entry3.place(relx=0.2,rely=0.4)
# lbl5=Label(root,text="Email",width=20,font=("bold",10))
# lbl5.place(relx=0.1,rely=0.5)
# entry4=Entry(root)
# entry4.place(relx=0.2,rely=0.5)
# lbl6=Label(root,text="phone no",width=20,font=("bold",10))
# lbl6.place(relx=0.1,rely=0.6)
# entry5=Entry(root)
# entry5.place(relx=0.2,rely=0.6)
# lbl7=Label(root,text="address",width=20,font=("bold",10))
# lbl7.place(relx=0.1,rely=0.7)
# entry6=Entry(root)
# entry6.place(relx=0.2,rely=0.7)
# lbl8=Label(text="Gender")
# lbl8.place(relx=0.143,rely=0.8)
# var=IntVar()
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(relx=0.2,rely=0.8)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(relx=0.266,rely=0.8)
# def data():
#    a=entry1.get()
#    b=entry2.get()
#    c=entry3.get()
#    d=entry4.get()
#    e=entry5.get()
#    f1=entry6.get()
#    gen=" "
#    if(var==1):
#       gen="male"
#    else:
#       gen="female"
#    f=open("std detail.txt","a")
#    f.write("\n"+a+" "+b+" "+c+" "+d+" "+e+" "+f1+" "+gen)
#    login()
# but=Button(root, text="Submit",width=20,activeforeground="blue",activebackground="violet",command=data).place(relx=0.3,rely=0.9)
# # but1=Button(root,text="login",width=20,activeforeground="blue",activebackground="violet",command=login).place(relx=0.3,rely=0.9)
# def login():
#     from tkinter import messagebox
#     root=Tk()
#     root.title("Login Form")
#     root.geometry("500x500")
#     l1=Label(root,text="Login Form",width=10,font=("bold",10))
#     l1.place(relx=0.1,rely=0.1)
#     l2=Label(root,text="Username",width=10,font=("bold",10))
#     l2.place(relx=0.1,rely=0.2)
#     e1=Entry(root)
#     e1.place(relx=0.2,rely=0.2)
#     l3=Label(root,text="Password",width=10,font=("bold",10))
#     l3.place(relx=0.1,rely=0.3)
#     e2=Entry(root)
#     e2.place(relx=0.2,rely=0.3)
#     def click():
#         a=e1.get()
#         b=e2.get()
#         f=open("std detail.txt","r")
#         data=f.read()
#         lines=data.split("\n")
#         for line in lines:
#             info=line.split()
#             if info[0]==a and info[1]==b:
#                 print("logged in")
#                 messagebox.showinfo("hello","login successfully")
#                 break
#         else:
#             print("nothing")
#             messagebox.showinfo("invalid","login Failed")
#     b1=Button(root,text="Submit",width=10,font=("bold",10),command=click).place(relx=0.1,rely=0.4)
#     root.mainloop()
# root.mainloop()







###login form


# from tkinter import*
# from tkinter import messagebox
# root=Tk()
# root.title("Login Form")
# root.geometry("500x500")
# l1=Label(root,text="Login Form",width=10,font=("bold",10))
# l1.place(relx=0.1,rely=0.1)
# l2=Label(root,text="Username",width=10,font=("bold",10))
# l2.place(relx=0.1,rely=0.2)
# e1=Entry(root)
# e1.place(relx=0.2,rely=0.2)
# l3=Label(root,text="Password",width=10,font=("bold",10))
# l3.place(relx=0.1,rely=0.3)
# e2=Entry(root)
# e2.place(relx=0.2,rely=0.3)
# def click():
#     a=e1.get()
#     b=e2.get()
#     f=open("bk.txt","r")
#     data=f.read()
#     lines=data.split("\n")
#     for line in lines:
#         info=line.split()
#         if info[3]==a and info[4]==b:
#             print("logged in")
#             messagebox.showinfo("hello","login successfully")
#             break
#     else:
#         print("nothing")
#         messagebox.showinfo("invalid","login Failed")
# b1=Button(root,text="Submit",width=10,font=("bold",10),command=click).place(relx=0.1,rely=0.4)
# b2=Button(root,text="Cancel",width=10,font=("bold",10),command=click).place(relx=0.2,rely=0.4)
# root.mainloop()




"""
f=open("st.txt","a")
f.write("\nname   \t pswd\n")
f.close()
 username="name"
password="pswd"
f=open("st.txt","r")
data=f.read()
lines=data.split("\n")
for line in lines:
    info=line.split()
    if info[0]==username and info[1]==password:
        print("logged in")
        break
else:
    print("nothing")"""


# from tkinter import*
# def check():
#     if(n.get()>0):
#         print("hi")
#     elif(n1.get()>2):
#         print("hlo")
#     else:
#         print("hai")
        
# f=open("std detail.txt","r")
# data=f.read()
# r=Tk()
# n=IntVar()
# c=Checkbutton(r,text="hi",variable=n,command=check).pack()
# n1=IntVar()
# c1=Checkbutton(r,text="hlo",variable=n1,command=check).pack()
# n2=IntVar()
# c2=Checkbutton(r,text="hai",variable=n2,command=check).pack()
# # f=open("std detail.txt","r")
# # print(f.read())
# btn=Button(r,text="enter",command=check).pack()

# r.mainloop()


    

# from tkinter import*
# def sel():
#     if var.get()==1:
#         print("male")
#     elif var.get()==2:
#         print("female")
#     else:
#         print("other")
#     select="you selected the option"+str(var.get())
#     Label.config(text=select)
# r=Tk()
# var=IntVar()
# r1=Radiobutton(r,text="option1",variable=var,value=1,command=sel)
# r1.pack(anchor=W)
# r2=Radiobutton(r,text="option2",variable=var,value=2,command=sel)
# r2.pack(anchor=W)
# r3=Radiobutton(r,text="option3",variable=var,value=3,command=sel)
# r3.pack(anchor=W)
# Label=Label(r)
# Label.pack()
# r.mainloop()




# root=Tk()
# root.geometry("1000x1000")
# frame=Frame(root,width=1000,height=1000,bg="gray")
# frame1=Frame(root,width=600,height=600,bg="cyan")
# font1=font.Font(root,weight="normal",family="Times new Roman",size=15)
# name=Label(root,text="Name",bg="orange",fg="black",font=font1)
# name.place(relx=0.15,rely=0.15,relwidth=0.15,relheight=0.05)
# nameentry=Entry(root)
# nameentry.place(relx=0.35,rely=0.15,relwidth=0.2,relheight=0.05)

# age=Label(root,text="Age",bg="orange",fg="black",font=font1)
# age.place(relx=0.15,rely=0.25,relwidth=0.15,relheight=0.05)
# ageentry=Entry(root)
# ageentry.place(relx=0.35,rely=0.25,relwidth=0.2,relheight=0.05)

# idno=Label(root,text="ID_Number",bg="orange",fg="black",font=font1)
# idno.place(relx=0.15,rely=0.35,relwidth=0.15,relheight=0.05)
# idnoentry=Entry(root)
# idnoentry.place(relx=0.35,rely=0.35,relwidth=0.2,relheight=0.05) 

# phoneno=Label(root,text="Contact_Number",bg="orange",fg="black",font=font1)
# phoneno.place(relx=0.15,rely=0.45,relwidth=0.15,relheight=0.05)
# phonenoentry=Entry(root)
# phonenoentry.place(relx=0.35,rely=0.45,relwidth=0.2,relheight=0.05)
# frame1.place(relx=0.1,rely=0.1)
# frame.place(relx=0,rely=0)

# submitbut=Button(root,text="submit",bg="orange",fg="white",font=font1,command=lambda:submit())
# submitbut.place(relx=0.5,rely=0.6,relwidth=0.09,relheight=0.06)
# clearbut=Button(root,text="clear",bg="orange",fg="white",font=font1,command=lambda:clear())
# clearbut.place(relx=0.4,rely=0.6,relwidth=0.09,relheight=0.06)
# viewbut=Button(root,text="View data",bg="orange",fg="white",font=font1,command=lambda:view())
# viewbut.place(relx=0.3,rely=0.6,relwidth=0.09,relheight=0.06)
# root.mainloop()

###Registration form


# from tkinter import *
# from tkinter import messagebox
# from tkinter import font
# from PIL import Image
# from PIL.ImageTk import PhotoImage
# root=Tk()
# root.geometry("1000x1000")
# labelfont=font.Font(family="Times New Roman",size=20,weight="bold")
# label=Label(root,text="Resgistration Form",background="purple",foreground="white",font=labelfont)
# label.place(relx=0.45,rely=0)
# name=Label(root,text="Name :")
# name.place(relx=0.05,rely=0.05)
# name1=Entry(root)
# name1.place(relx=0.17,rely=0.05)

# email=Label(root,text="Email ID :")
# email.place(relx=0.05,rely=0.09)
# email1=Entry(root)
# email1.place(relx=0.17,rely=0.09,relwidth=0.2)

# pn=Label(root,text="Phone number :")
# pn.place(relx=0.05,rely=0.13)
# pn1=Entry(root)
# pn1.place(relx=0.17,rely=0.13)

# g=Label(root,text="Gender :")
# g.place(relx=0.05,rely=0.17)

# gender=IntVar()
# g1=Radiobutton(root,text="Male",variable=gender,value=1)
# g1.place(relx=0.17,rely=0.17)
# g2=Radiobutton(root,text="Female",variable=gender,value=2)
# g2.place(relx=0.25,rely=0.17)
# g3=Radiobutton(root,text="Others",variable=gender,value=3)
# g3.place(relx=0.34,rely=0.17)

# g=Label(root,text="Department :")
# g.place(relx=0.05,rely=0.21)

# degree=IntVar()
# d1=Radiobutton(root,text="CSE",variable=degree,value=1)
# d1.place(relx=0.17,rely=0.21)
# d2=Radiobutton(root,text="ECE",variable=degree,value=2)
# d2.place(relx=0.25,rely=0.21)
# d3=Radiobutton(root,text="MECH",variable=degree,value=3)
# d3.place(relx=0.34,rely=0.21)
# d4=Radiobutton(root,text="ICE",variable=degree,value=4)
# d4.place(relx=0.42,rely=0.21)
# d5=Radiobutton(root,text="EEE",variable=degree,value=5)
# d5.place(relx=0.48,rely=0.21)
# d6=Radiobutton(root,text="IT",variable=degree,value=6)
# d6.place(relx=0.56,rely=0.21)

# location=Label(root,text="Location :")
# location.place(relx=0.05,rely=0.25)

# p1=Checkbutton(root,text="Chennai")
# p1.place(relx=0.17,rely=0.25)
# p2=Checkbutton(root,text="Banglore")
# p2.place(relx=0.17,rely=0.29)
# p3=Checkbutton(root,text="Trichy")
# p3.place(relx=0.17,rely=0.33)
# p4=Checkbutton(root,text="Thuthukudi")
# p4.place(relx=0.17,rely=0.37)
# p5=Checkbutton(root,text="Madurai")
# p5.place(relx=0.17,rely=0.41)

# img=PhotoImage(Image.open("kkk.jpg"))
# img1=Label(root,image=img)
# img1.place(relx=0.5,rely=0.25)

# i=Label(root,text="Interview Experience")
# i.place(relx=0.05,rely=0.45)

# check=IntVar()
# i1=Radiobutton(root,text="Yes",variable=check,value=1,)
# i1.place(relx=0.17,rely=0.45)
# i2=Radiobutton(root,text="No",variable=check,value=2,)
# i2.place(relx=0.21,rely=0.45)

# address=Label(root,text="Address : ")
# address.place(relx=0.05,rely=0.49)
# address1=Text(root,height=3,width=30)
# address1.place(relx=0.17,rely=0.49)

# def finish():
#     messagebox.showinfo("Thank you","submitted")

# btn=Button(root,text="Submit",command=finish)
# btn.place(relx=0.9,rely=0.7)


#root.mainloop()

###register



# import tkinter
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import ImageTk,Image
# win=Tk()
# win.geometry("500x500")
# frame=Frame(win,width=200,height=100)
# frame.pack()
# frame.place(relx=0.3,rely=0)
# img=ImageTk.PhotoImage(Image.open("registerimg.jpg"))
# label=Label(frame,image=img)
# label.pack()

# l1=Label(win,text="Name")
# l1.place(relx=0.05,rely=0.5)
# l2=Label(win,text="Father Name")
# l2.place(relx=0.05,rely=0.6)
# l3=Label(win,text="Email-ID")
# l3.place(relx=0.05,rely=0.7)
# l4=Label(win,text="Mobile No")
# l4.place(relx=0.05,rely=0.8)

# e1=Entry(win)
# e1.place(relx=0.2,rely=0.5)
# e2=Entry(win)
# e2.place(relx=0.2,rely=0.6) 
# e3=Entry(win)
# e3.place(relx=0.2,rely=0.7)
# e4=Entry(win)
# e4.place(relx=0.2,rely=0.8)   

# r=Label(win,text="Gender")
# r.place(relx=0.5,rely=0.5)
# var=IntVar()
# r1=Radiobutton(win,text="Male",variable=var,value=1)
# r1.place(relx=0.6,rely=0.5)
# r2=Radiobutton(win,text="Female",variable=var,value=2)
# r2.place(relx=0.7,rely=0.5)

# c1=Label(win,text="city")
# c1.place(relx=0.5,rely=0.6)
# combo=ttk.Combobox(win,values=["Mayiladuthurai","Thanjavur","Thiruvarur","Nagapattinam","Madurai","Chennai"])
# combo.place(relx=0.6,rely=0.6)

# t1=Label(win,text="Address")
# t1.place(relx=0.5,rely=0.7)
# t2=Text(win,height=2,width=30)
# t2.place(relx=0.6,rely=0.7)
# t3=Label(win,text="Remarks")
# t3.place(relx=0.5,rely=0.8)
# t4=Text(win,height=2,width=18)
# t4.place(relx=0.6,rely=0.8) 

# def func():
#     messagebox.showinfo("Registration","Registered Successfully")
# def reg():
#     f=open('bk.txt','a')
#     f.write('\n')
#     f.write(e1.get())
#     f.write('\t')
#     f.write(e2.get())
#     f.write('\t')
#     f.write(e3.get())
#     f.write('\t')
#     f.write(e4.get())
#     f.write('\t')
#     if var.get()==1:
#         f.write("Male")
#     else:
#         f.write("Female")
#     f.write('\t') 
#     f.write(str(combo.get()))
#     f.write('\t')
#     f.write(str(t2.get(1.0,END)))
#     f.write('\t')
#     f.write(str(t4.get(1.0,END)))
#     f.write('\t')
#     func()
    
# img1=ImageTk.PhotoImage(Image.open("regr.jpg"))
# label1=Button(win,image=img1,activebackground="red",command=reg)
# label1.place(relx=0.6,rely=0.9)

# win.mainloop()




# from tkinter import *
# from tkinter import messagebox

# root=Tk()

# l1=Label(root,text="Name")
# l1.grid(row=0,column=1)
# l2=Label(root,text="Father Name")
# l2.grid(row=1,column=1)
# l3=Label(root,text="Age")
# l3.grid(row=2,column=1)
# l4=Label(root,text="Degree")
# l4.grid(row=3,column=1)
# l5=Label(root,text="Address")
# l5.grid(row=4,column=1)
# text=Text(root,height=3,width=30)
# text.grid(row=4,column=2)
# l6=Label(root,text="Gender")
# l6.grid(row=5,column=1)
# l7=Label(root,text="Physically Challenged Person")
# l7.grid(row=6,column=1)
# l8=Label(root,text="Sports Quota")
# l8.grid(row=7,column=1)

# e1=Entry(root)
# e1.grid(row=0,column=2)
# e2=Entry(root)
# e2.grid(row=1,column=2)
# e3=Entry(root)
# e3.grid(row=2,column=2)

# checkbox1=IntVar()
# checkbox2=IntVar()
# checkbox3=IntVar()


# c1=Checkbutton(root,text="UG",variable=checkbox1,onvalue=1,offvalue=0,height=1,width=10)
# c1.grid(row=3,column=2)
# c2=Checkbutton(root,text="PG",variable=checkbox2,onvalue=1,offvalue=0,height=1,width=10)
# c2.grid(row=3,column=3)
# c3=Checkbutton(root,text="other",variable=checkbox3,onvalue=1,offvalue=0,height=1,width=10)
# c3.grid(row=3,column=4)

# var=IntVar()
# var1=IntVar()
# var2=IntVar()
# r1=Radiobutton(root,text="Male",variable=var,value=1)
# r1.grid(row=5,column=2)
# r2=Radiobutton(root,text="Female",variable=var,value=2)
# r2.grid(row=5,column=3)
# r3=Radiobutton(root,text="Transgender",variable=var,value=3)
# r3.grid(row=5,column=4)

# r1=Radiobutton(root,text="Yes",variable=var1,value=1)
# r1.grid(row=6,column=2)
# r2=Radiobutton(root,text="No",variable=var1,value=2)
# r2.grid(row=6,column=3)

# r1=Radiobutton(root,text="Yes",variable=var2,value=1)
# r1.grid(row=7,column=2)
# r2=Radiobutton(root,text="No",variable=var2,value=2)
# r2.grid(row=7,column=3)

# def name():
#     f=open("std.txt","a")
#     f.write('\n')
#     f.write(e1.get())
#     f.write('\t')
#     f.write(e2.get())
#     f.write('\t')
#     f.write(e3.get())
#     f.write('\t')
#     f.write(str(var.get()))
#     f.write('\t')
#     f.write(str(var1.get()))
#     f.write('\t')
#     f.write(str(var2.get()))
#     f.write('\t')
    
#     f.write(str(checkbox1.get()))
#     f.write("\t")
#     f.write(str(checkbox2.get()))
#     f.write("\t")
#     f.write(str(checkbox3.get()))
#     f.write("\t")
#     f.write(str(text.get(1.0,END)))
#     f.write('\t')

# button=Button(root,text="register",command=name)
# button.grid(row=8,column=0)

# root.mainloop()


























    
    
