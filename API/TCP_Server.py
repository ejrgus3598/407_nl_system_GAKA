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
            # 30개 보정식(지금 FULL_CONTROL하던건 이걸로.)
            # if(num == 1) :
            #     cct = (1.24498696*cct)-1105.423232
            # elif (num == 2) :
            #     cct = (1.24062724*cct)-1106.674882
            # elif (num == 3) :
            #     cct = (1.25937117*cct)-1090.490959
            # elif (num == 4) :
            #     cct = (1.27553676*cct)-1174.399201
            # elif (num == 5) :
            #     cct = (1.19333697*cct)-1105.055017
            # elif (num == 6) :
            #     cct = (1.12704578*cct)-1062.479705
            # elif (num == 7) :
            #     cct = (1.1664019*cct)-1124.688802
            # elif (num == 8) :
            #     cct = (1.235*cct)-1085.5
            # elif (num == 9) :
            #     cct = (1.18249764*cct)-1139.85934302

            # 요건 세현이형 하던 보정식
            if (num == 1):
                cct = (1.1062 * cct) - 618.65
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
        except Exception as err:
            print(err)
            # Send response message for file not found
            # connectionSocket.send('404 Not Found')
            # Close client socket
            print("socket close")
            connectionSocket.close()
    serverSocket.close()

if __name__ == '__main__':
    process()

