import serial, time
arduino = serial.Serial("COM3", 9600)
time.sleep(2)
arduino.write(b'N')
arduino.close()