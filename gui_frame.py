
# from tkinter import*
# name=Tk()
# frame=Frame(name,bg="violet",width=80,height=70)
# frame.pack()
# name.mainloop()

###another

# from tkinter import*
# name=Tk()
# f1=Frame(name)
# f2=Frame(name)
# for i in["blue","red","violet","pink","white","black"]:
#     Frame(name,height=10,width=20,bg=i).pack()
#     f1.pack(padx=50,pady=70)
#     f2.pack(padx=70,pady=40)
# name.mainloop()




##doubleframe

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
