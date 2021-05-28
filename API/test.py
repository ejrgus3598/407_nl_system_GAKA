from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('192.168.100.100', 80))
serverSocket.listen(80)
while True:
    print('Ready to serve...')
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message.decode())
        #Send one HTTP header line into socket
        # connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
    except IOError:
        #Send response message for file not found
        # connectionSocket.send('404 Not Found')
        #Close client socket
        print("socket close")
        connectionSocket.close()
serverSocket.close()