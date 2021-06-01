from socket import *
from Core.arduino_color_sensor import acs

def process():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    serverSocket.bind(('192.168.100.100', 80))
    serverSocket.listen(80)

    acs1 = acs.getInstance()

    while True:
        # print('Ready to serve...')
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            str = message.decode().split("\n")[5].split("&")
            # print(str)
            num = int(str[0].split("=")[1])
            illum = float(str[1].split("=")[1])
            cct = float(str[2].split("=")[1])
            # print(num, "번 들어옴")
            if (num == 1):
                cct = (1.1062 * cct) - 618.65
                # acs1.get_sensor_data()
            elif (num == 2):
                cct = (1.1011 * cct) - 617.02
            elif (num == 3):
                cct = (1.1201 * cct) - 595.18
            elif (num == 4):
                cct = (1.1304 * cct) - 677.1
            elif (num == 5):
                cct = (1.0591 * cct) - 607.35
            elif (num == 6):
                cct = (1.0066 * cct) - 574.18
            elif (num == 7):
                cct = (1.0347 * cct) - 619.09
            elif (num == 8):
                cct = (1.0889 * cct) - 573.73
            elif (num == 9):
                cct = (1.0452 * cct) - 602.95
            elif (num == 10):
                cct = (1.0639 * cct) - 542.35

            # insert_db("cct",num, illum, cct)
            acs1.set_sensor_data(num, illum, cct)

            # Send one HTTP header line into socket
            # connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
        except IOError:
            # Send response message for file not found
            # connectionSocket.send('404 Not Found')
            # Close client socket
            print("socket close")
            connectionSocket.close()
    serverSocket.close()

if __name__ == '__main__':
    process()

