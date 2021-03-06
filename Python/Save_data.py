'''
This program is used to get train data to put inside the Vector machine.
It saves the data from the Arduino serial port to a CSV file. 
The dictionary key 'activity' indicates what motion the user is doing 
this allows the Support Vector Machine to distinguish different movements.
'''

import serial
import pandas as pd
import csv

device = serial.Serial("COM5", baudrate = 115200)
accx = []
accy = []
accz = []

accx_2=[]
accy_2=[]
accz_2=[]

gyrox = []
gyroy = []
gyroz = []

gyrox_2 = []
gyroy_2 = []
gyroz_2 = []

mag_acc = []
mag_acc_2 = []
mag_gyro = []
mag_gyro_2 = []

angle = []

# user current activity
standing = 1
laying = 2
sitting = 3
walking = 4
upstairs = 5
downstairs = 6
falling = 7


dict = {'acclx':accx,'accly':accy,'acclz':accz,
    'acclx2':accx_2,'accly2':accy_2,'acclz2':accz_2,
    'gyrx':gyrox,'gyry':gyroy,'gyrz':gyroz,
    'gyrx2':gyrox_2,'gyry2':gyroy_2,'gyrz2':gyroz_2,
    'magnitude_acc': mag_acc,'magnitude_acc2' :mag_acc_2,
    'magnitude_gyro':mag_gyro,'magnitude_gyro2': mag_gyro_2,
    'angle_displament':angle,'activity':downstairs}


while 1:
    while device.inWaiting() == 0:
        pass

    byte = device.readline()
    s = byte[0:-2].decode("utf-8")
    x = s.split(",")
    print(x)

    accx.append(float(x[0]))
    accy.append(float(x[1]))
    accz.append(float(x[2]))

    accx_2.append(float(x[3]))
    accy_2.append(float(x[4]))
    accz_2.append(float(x[5]))

    gyrox.append(float(x[6]))
    gyroy.append(float(x[7]))
    gyroz.append(float(x[8]))

    gyrox_2.append(float(x[9]))
    gyroy_2.append(float(x[10]))
    gyroz_2.append(float(x[11]))

    mag_acc.append(float(x[12]))
    mag_acc_2.append(float(x[13]))

    mag_gyro.append(float(x[14]))
    mag_gyro_2.append(float(x[15]))
    
    angle.append(float(x[16]))

    df = pd.DataFrame(dict)
    df.to_csv('Train_Data.csv')
