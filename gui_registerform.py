
from tkinter import*
root=Tk()
root.attributes('-fullscreen', True)
root.title("Registraction From")
root.geometry("50x50")
l=Label(root,text="Registraction From",width=20,bg="violet",fg="blue",font=("bold",20)).grid(row=0,column=1)
l2=Label(root,text="Name",width=20,bg="orange",fg="green",font=("bold",10)).grid(row=1,column=1)
e1=Entry(root)
e1.grid(row=0,column=2)
l3=Label(root,text="Age",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=1,column=1)
e2=Entry(root)
e2.grid(row=1,column=2)
l4=Label(root,text="DOB",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=2,column=1)
e3=Entry(root)
e3.grid(row=2,column=2)
l5=Label(root,text="Phone no",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=3,column=1)
e4=Entry(root)
e4.grid(row=3,column=2)
l6=Label(root,text="Email id",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=4,column=1)
e5=Entry(root)
e5.grid(row=4,column=2)
l7=Label(root,text="Gender",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=5,column=1)
e6=Entry(root)
e6.grid(row=5,column=2)
l7=Label(root,text="Aadhar no",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=6,column=1)
e7=Entry(root)
e7.grid(row=6,column=2)
l8=Label(root,text="Address",width=10,bg="orange",fg="green",font=("bold",10)).grid(row=7,column=1)
e8=Entry(root)
e8.grid(row=7,column=2)
def data():
    a=e1.get()
    b=e1.get()
    c=e1.get()
    d=e1.get()
    e=e1.get()
    f1=e1.get()
    h=e1.get()
    i=e1.get()
    f=open("set.txt","a")
    f.write(a+" "+b+" "+c+" "+d+" "+e+" "+f1+" "+h+" "+i)
but=Button(root,text="Click",width=20,bg="pink",fg="blue",font=("bold",5),command=data).grid(row=8,column=2)
but1=Button(root,text="exit",command=root.destroy ).grid(row=9,column=3)
root.mainloop()






# from tkinter import *


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