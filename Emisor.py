import socket
import struct
import serial, time

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

arduino = serial.Serial('COM3', 9600)

MULTICAST_TTL = struct.pack('b', 1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

time.sleep(1)

message_arduino_anterior = 'P'

while (True):
    message_ardui = arduino.readline()
    message_arduino = message_ardui.decode('utf-8')
    #print(message_arduino)

    #Codifica el mensaje a bytes
    bytes_message = str.encode(message_arduino) 

    #print(" ")

    print(bytes_message)

    if (message_arduino != message_arduino_anterior):
        sock.sendto(bytes_message, (MCAST_GRP, MCAST_PORT))
        
    message_arduino_anterior = message_arduino
    
sock.close()