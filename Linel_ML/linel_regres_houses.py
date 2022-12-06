import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def show_plant(df):
    plt.scatter(df.area, df.price)
    plt.xlabel('Площадь (кв.м.)')
    plt.ylabel('Стоимость(млн.руб)')
    plt.plot(df.area, reg.predict(df[['area']]))
    plt.show() 

df = pd.read_excel('data.xlsx')

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
#print(reg.predict([[120]])) Вывод предсказания


pred = pd.read_excel('predict.xlsx')

p = reg.predict(pred)
pred['price'] = p 
show_plant(df)
pred.to_excel('new.xlsx', index= False)


