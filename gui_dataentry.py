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


##another (multuiple function)

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


# # arithmetic operator
# import tkinter
# from tkinter import *
# from tkinter import messagebox

# r=Tk()
# r.geometry("400x400")
# l1=Label(r,text="Enter the first value")
# l1.grid(row=0,column=1)
# l2=Label(r,text="Enter the second value")
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
#     e3.delete(0,50)
#     e3.insert(0,c)
# def sub():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a-b
#     e3.delete(0,50)
#     e3.insert(0,c)
# def mul():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a*b
#     e3.delete(0,50)
#     e3.insert(0,c)
# def div():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a/b
#     e3.delete(0,50)
#     e3.insert(0,c)
#     messagebox.showinfo("textbox","valid-successfully")

# b=Button(r,text="Sub",bg="pink",command=lambda:sub())
# b.grid(row=0,column=3)

# b=Button(r,text="Add",bg="red",command=lambda:add())
# b.grid(row=1,column=3)

# b=Button(r,text="Mul",bg="green",command=lambda:mul())
# b.grid(row=2,column=3)

# b=Button(r,text="Div",bg="yellow",command=lambda:div())
# b.grid(row=3,column=3)

# r.mainloop()