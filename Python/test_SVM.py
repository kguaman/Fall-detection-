'''
I used jupyter notebook to create and test the SVM accuracy
information to install Jupyter Notebook can be found here -> https://jupyter.org/install

After collecting train data and test data I created an SVM to test whether the Support Vector Machine can accurately classify different movements.
'''

import pandas as pd
%matplotlib inline
#%matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.svm import SVR

train = pd.read_csv(r'train_data.csv',index_col = 0)
test = pd.read_csv(r'testdata.csv',index_col = 0)

X_train = train.iloc[:,1:11]
Y_train =train['activity']
X_test =test.iloc[:, 1:11]
Y_test =test['activity']

# SVM
sc = StandardScaler().fit(X_train)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
ML = svm.SVC(kernel = 'rbf',gamma = .01,C= 1).fit(X_train,Y_train)
'''
compare the real-time data from the senor to the SVM 
'''
outcome = ['standing', 'laying', 'sitting', 'walking', 'upstairs', 'downstairs', 'falling']
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
    if outcome[y_test_pred] == 'falling':
         device.write("f")
    else:
        device.write("n")


'''
display a table actual col and Predicted col 
use to check accuarcy of SVM :

y_test_pred=ML.predict(X_test)
y_test_pred

df=pd.DataFrame({'Actual':Y_test, 'Predicted':y_test_pred})
df.head(30)

# accuracy value
accuracy=accuracy_score(Y_test,y_test_pred)
accuracy = accuracy * 100
print(int(accuracy))

# plots a matrix 
plot_confusion_matrix(ML, X_test, Y_test,) 

'''

