
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from subprocess import check_call


df=pd.read_csv('csv_eco.csv')
col2=df.columns.values.tolist()

df=df.replace("R",1)
df=df.replace("S",0)
df=df.replace("I",0)
df=df.replace("ND",0)
df=df.replace("ND    ",0)
df=df.replace("F",1)
df=df.replace(" F",1)
df=df.replace("M",0)
df=df.replace("M ",0)
df=df.replace('Pus',0)
df=df.replace('Urine',1)
df=df.replace('Blood',2)
df=df.replace('Sputum',3)


X = df[['Gender', 'Age','Meropenem ','Cefotaxime']]
Y = df['Imipenem']


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_gini = DecisionTreeClassifier(criterion = "entropy", random_state = 100)
clf_gini.fit(X_train, y_train)

DecisionTreeClassifier(criterion='entropy', random_state=100, splitter='best',)

y_pred = clf_gini.predict(X_test)
#print ("\n\n\nAccuracy is ", accuracy_score(y_test,y_pred)*100, " \n\n\n")
#print (clf_gini.predict([[1, 45,0,0,0]]))


def pred(det1, det2, det3, det4):
    return clf_gini.predict([[det1, det2, det3, det4]])

#result = pred(0, 45, 0, 0)
#print ("\n\n\n",result[0])


