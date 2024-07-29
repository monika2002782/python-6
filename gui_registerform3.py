##Registration form


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