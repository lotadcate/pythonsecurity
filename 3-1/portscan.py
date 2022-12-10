import socket, sys
ip = sys.argv[1]
ports = range(7995, 8001)

for port in ports:
  sock = socket.socket()
  ret = sock.connect_ex((ip, port))
  print(ret)
  if ret == 0:
    print(str(port) + " open")
