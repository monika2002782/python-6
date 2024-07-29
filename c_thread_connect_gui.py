# from tkinter import*
# import socket
# import threading
# import time


# r=Tk()
# r.title("client")
# r.geometry("500x500")
# l=Label(r,text="port_address").place(relx=0.1,rely=0.1)
# e=Entry(r).place(relx=0.288,rely=0.1)


# def client():
#         s=socket.socket()
#         host=socket.gethostname()
#         port=12345
#         s.connect((host,port))
#         a=s.recv(1024)
#         print(a.decode()+"i am a client one")
#         s.close()
# b=Button(r,text="connect",command=lambda:client()).place(relx=0.2,rely=0.2)
# r.mainloop()


# thread2=threading.Thread(target=client)
# thread2.start()
# thread2.join()

# print("both thread have finished")