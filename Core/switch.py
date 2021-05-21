# socket module import!
import socket

# socket create and connection
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("192.168.100.150", 5000))

# send msg
# 0은 릴레이 off, 1은 릴레이 0
test_msg = "0"
sock.send(test_msg.encode())

time.sleep(2)
test_msg = "1"
sock.send(test_msg.encode())
# # recv data
# data_size = 512
# data = sock.recv(data_size)

# connection close
sock.close()