import serial, time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)
while(True):
    rawString = arduino.readline()
    raw_string_s = rawString.decode('utf-8')
    print(raw_string_s)
arduino.close()