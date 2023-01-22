import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()                           
port = 12345

s.bind((host, port))                                  
s.listen(5)                                           


while True:
  # establish a connection
  c, addr = s.accept()
  print('Got connection from', addr)

  total = 0
  while True:
    data = c.recv(1024)
    if not data:
      break
    data = data.decode()
    print(data)
    if data == "FINISH":
      break
    total += int(data)

  print("The sum of the received numbers is: ", total)
  c.close()