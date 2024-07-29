from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()


##anohter

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
