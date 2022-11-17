import socket
import struct
import serial, time

MCAST_GRP = '224.0.0.2'
MCAST_PORT = 5004
IS_ALL_GROUPS = True

arduino = serial.Serial('COM3', 9600)

time.sleep(2)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind(('', MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


while True:

  mensaje_de_emisor = sock.recv(255)

  print(mensaje_de_emisor)
  
  arduino.write(mensaje_de_emisor)
        