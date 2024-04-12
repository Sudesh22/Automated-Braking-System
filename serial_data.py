import serial

ser = serial.Serial("COM11", 9600)
def get_data():
    value = ser.readline().decode()
    # print(str(value)[2:-5])
    print(value)

while 1:
    get_data()