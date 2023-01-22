import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 12345

s.connect((host, port))
done = False
while not done:
    #generate random numbers and send them to the receiver
    num = random.randint(1, 100)
    s.sendall(str(num).encode())
    response = input("Are you done sending numbers? (y/n)")
    if response == 'y':
        done = True
        s.sendall("FINISH".encode())

s.close()
