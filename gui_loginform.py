

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



# import tkinter as tk
# from tkinter import messagebox

# # Function to validate the login
# def validate_login():
#     userid = username_entry.get()
#     password = password_entry.get()

#     # You can add your own validation logic here
#     if userid == "moni" and password == "navi":
#         messagebox.showinfo("Login Successful", "Welcome, Admin!")
#     else:
#         messagebox.showerror("Login Failed", "Invalid username or password")

# # Create the main window
# parent = tk.Tk()
# parent.title("Login Form")

# # Create and place the username label and entry
# username_label = tk.Label(parent, text="Userid:")
# username_label.pack()

# username_entry = tk.Entry(parent)
# username_entry.pack()

# # Create and place the password label and entry
# password_label = tk.Label(parent, text="Password:")
# password_label.pack()

# password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
# password_entry.pack()

# # Create and place the login button
# login_button = tk.Button(parent, text="Login", command=validate_login)
# login_button.pack()

# # Start the Tkinter event loop
# parent.mainloop()