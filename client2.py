import socket
s=socket.socket()
host=socket.gethostname()
port=54321
s.connect((host,port))
a=s.recv(1024)
print(a.decode()+"I am a client two")
s.close()
