from tkinter import *
from tkinter import messagebox

root=Tk()

l1=Label(root,text="Name")
l1.grid(row=0,column=1)
l2=Label(root,text="Father Name")
l2.grid(row=1,column=1)
l3=Label(root,text="Age")
l3.grid(row=2,column=1)
l4=Label(root,text="Degree")
l4.grid(row=3,column=1)
l5=Label(root,text="Address")
l5.grid(row=4,column=1)
text=Text(root,height=3,width=30)
text.grid(row=4,column=2)
l6=Label(root,text="Gender")
l6.grid(row=5,column=1)
l7=Label(root,text="Physically Challenged Person")
l7.grid(row=6,column=1)
l8=Label(root,text="Sports Quota")
l8.grid(row=7,column=1)

e1=Entry(root)
e1.grid(row=0,column=2)
e2=Entry(root)
e2.grid(row=1,column=2)
e3=Entry(root)
e3.grid(row=2,column=2)

checkbox1=IntVar()
checkbox2=IntVar()
checkbox3=IntVar()


c1=Checkbutton(root,text="UG",variable=checkbox1,onvalue=1,offvalue=0,height=1,width=10)
c1.grid(row=3,column=2)
c2=Checkbutton(root,text="PG",variable=checkbox2,onvalue=1,offvalue=0,height=1,width=10)
c2.grid(row=3,column=3)
c3=Checkbutton(root,text="other",variable=checkbox3,onvalue=1,offvalue=0,height=1,width=10)
c3.grid(row=3,column=4)

var=IntVar()
var1=IntVar()
var2=IntVar()
r1=Radiobutton(root,text="Male",variable=var,value=1)
r1.grid(row=5,column=2)
r2=Radiobutton(root,text="Female",variable=var,value=2)
r2.grid(row=5,column=3)
r3=Radiobutton(root,text="Transgender",variable=var,value=3)
r3.grid(row=5,column=4)

r1=Radiobutton(root,text="Yes",variable=var1,value=1)
r1.grid(row=6,column=2)
r2=Radiobutton(root,text="No",variable=var1,value=2)
r2.grid(row=6,column=3)

r1=Radiobutton(root,text="Yes",variable=var2,value=1)
r1.grid(row=7,column=2)
r2=Radiobutton(root,text="No",variable=var2,value=2)
r2.grid(row=7,column=3)

def name():
    f=open("std.txt","a")
    f.write('\n')
    f.write(e1.get())
    f.write('\t')
    f.write(e2.get())
    f.write('\t')
    f.write(e3.get())
    f.write('\t')
    f.write(str(var.get()))
    f.write('\t')
    f.write(str(var1.get()))
    f.write('\t')
    f.write(str(var2.get()))
    f.write('\t')
    
    f.write(str(checkbox1.get()))
    f.write("\t")
    f.write(str(checkbox2.get()))
    f.write("\t")
    f.write(str(checkbox3.get()))
    f.write("\t")
    f.write(str(text.get(1.0,END)))
    f.write('\t')

button=Button(root,text="register",command=name)
button.grid(row=8,column=0)

root.mainloop()



