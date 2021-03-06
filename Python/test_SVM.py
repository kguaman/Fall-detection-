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

X_train = train.iloc[:,1:9]
Y_train =train['activity']
X_test =test.iloc[:, 1:9]
Y_test =test['activity']

# SVM
sc = StandardScaler().fit(X_train)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
ML = svm.SVC(kernel = 'rbf',gamma = .01,C= 1).fit(X_train,Y_train)

y_test_pred=ML.predict(X_test)
y_test_pred

'''
display a table actual col and Predicted col 
use to check accuarcy of SVM :
'''

df=pd.DataFrame({'Actual':Y_test, 'Predicted':y_test_pred})
df.head(30)

# accuracy value
accuracy=accuracy_score(Y_test,y_test_pred)
accuracy = accuracy * 100
print(int(accuracy))

# plots a matrix 
plot_confusion_matrix(ML, X_test, Y_test,) 
