
outcome = ["standing", "laying", "sitting", "walking", "upstairs", "downstairs", "falling"]
device = serial.Serial('COM5',baudrate = 115200)

while 1:
    while device.inWaiting() == 0:
        pass 
    
    byte = device.readline()
    temp = byte[0:-2].decode("utf-8")
    x = temp.split(',')
    print(x)
    data_1 = x[0]
    data_2 = x[1]
    data_3 = x[2]
    data_4 = x[3]
    data_5 = x[4]
    data_6 = x[5]
    data_7 = x[12]
    data_8 = x[13]
    data_9 = x[14]
    data_10 = x[15]
    data_11 = x[16]
    
    
    Test = [[data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,data_11]]
    y_test_pred=ML.predict(Test)
    print('SVM result:')
    print(outcome[y_test_pred])
    if outcome[y_test_pred] == falling:
         device.write("f")
    else:
        device.write("n")
