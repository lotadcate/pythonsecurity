import socket

sock = socket.socket(
         socket.AF_INET,
         socket.SOCK_STREAM
       )

ip = "127.0.0.1"
port = 50000

server = (ip, port)
sock.connect(server)

msg = ""
while msg != 'exit':
  msg = input("-> ")

  sock.send(msg.encode()) # データをサーバに送信
  data = sock.recv(1024) # サーバからデータを受信

  print("Received from server: " + str(data))

sock.close()

