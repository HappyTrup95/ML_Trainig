from sklearn import tree
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

df_tr = pd.read_csv(r'https://stepik.org/media/attachments/course/4852/dogs_n_cats.csv')

X = df_tr.drop(['Вид'], axis=1)
y = df_tr['Вид']
X_train, X_test, y_train, y_test =  train_test_split(X,y,test_size=0.33,random_state=42)
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
clf.fit(X_train,y_train)
df_ts = pd.read_json(r'https://stepik.org/api/attempts/759949141/file')
df_ts[:2]
df_tr[:2]
X_ts = df_ts[['a', 'b', 'c', 'd']]
result = clf.predict(X_ts)
print(pd.Series(result)[result == 'собачка'].count())