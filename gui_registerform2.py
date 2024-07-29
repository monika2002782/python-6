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


