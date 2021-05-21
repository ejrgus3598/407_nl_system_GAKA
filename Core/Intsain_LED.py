# LED 제어, DB에 누적
import socket
import numpy as np

global LED_state
LED_state = np.zero(30,5)

def set_LED(num, ch1, ch2, ch3, ch4):
    global LED_state
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "AT+CONTROL=FLAT_PWM,A,%d,%d,%d,%d,%d\r\n" % (num, ch1, ch2, ch3, ch4)
    LED_state[num] = [num, ch1, ch2, ch3, ch4]
    print(LED_state[num])
    sock.sendto(msg.encode(), ("192.168.100.210", 50210))
    sock.close()

def all_set_LED(ch1, ch2, ch3, ch4):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(30):
        msg = "AT+CONTROL=FLAT_PWM,A,%d,%d,%d,%d,%d\r\n" % (i, ch1, ch2, ch3, ch4)
        LED_state[i] = [i, ch1, ch2, ch3, ch4]
        print(LED_state[i])
        sock.sendto(msg.encode(), ("192.168.100.210", 50210))
    sock.close()


