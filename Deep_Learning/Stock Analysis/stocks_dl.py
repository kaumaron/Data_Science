import numpy as np
import pandas as pd
import talib

## Because of Mac OS X and not using an Jupyter Notebook
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import random
random.seed(42)

from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

dataset = pd.read_csv(r'/Users/akdm/Documents/Data Science/DataScienceGit/'+\
                        r'Deep_Learning/Stock Analysis/ANN-Stock-Prediction-Python-Code_Reliance'+
                        r'/RELIANCE.NS.csv')
dataset = dataset.dropna()
dataset = dataset[['Open','High','Low','Close']]

dataset['H-L'] = dataset['High'] - dataset['Low']
dataset['O-C'] = dataset['Close'] - dataset['Open']
dataset['3day MA'] = dataset['Close'].shift(1).rolling(window = 3).mean()
dataset['10day MA'] = dataset['Close'].shift(1).rolling(window = 10).mean()
dataset['30day MA'] = dataset['Close'].shift(1).rolling(window = 30).mean()
dataset['Std_dev']= dataset['Close'].rolling(5).std()
dataset['RSI'] = talib.RSI(dataset['Close'].values, timeperiod = 9)
dataset['Williams %R'] = talib.WILLR(dataset['High'].values, dataset['Low'].values, dataset['Close'].values, 7)

dataset['Price_Rise'] = np.where(dataset['Close'].shift(-1) > dataset['Close'], 1, 0)

dataset = dataset.dropna()

X = dataset.iloc[:, 4:-1]
y = dataset.iloc[:, -1]

split = int(len(dataset) * 0.8)
X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = Sequential()
classifier.add(Dense(units = 128,
                    kernel_initializer = 'uniform',
                    activation = 'relu',
                    input_dim = X.shape[1]))

classifier.add(Dense(units = 1,
                    kernel_initializer = 'uniform',
                    activation = 'relu'))

classifier.compile(optimizer = 'adam',
                    loss = 'mean_squared_error',
                    metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

dataset['y_pred'] = np.NaN
dataset.iloc[(len(dataset) - len(y_pred)):,-1:] = y_pred
trade_dataset = dataset.copy().dropna()

trade_dataset.loc[:,'Tomorrows Returns'] = 0.
trade_dataset.loc[:,'Tomorrows Returns'] = np.log(trade_dataset['Close']/\
                                        trade_dataset['Close'].shift(1))
trade_dataset.loc[:,'Tomorrows Returns'] = trade_dataset['Tomorrows Returns'].shift(-1)

trade_dataset.loc[:,'Strategy Returns'] = 0.
trade_dataset.loc[:,'Strategy Returns'] = np.where(
                                    trade_dataset['y_pred'] == True,
                                    trade_dataset['Tomorrows Returns'],
                                    - trade_dataset['Tomorrows Returns']
                                    )


trade_dataset.loc[:,'Cumulative Market Returns'] = np.cumsum(trade_dataset['Tomorrows Returns'])
trade_dataset.loc[:,'Cumulative Strategy Returns'] = np.cumsum(trade_dataset['Strategy Returns'])

plt.figure(figsize=(10,5))
plt.plot(trade_dataset['Cumulative Market Returns'], color='r', label='Market Returns')
plt.plot(trade_dataset['Cumulative Strategy Returns'], color='g', label='Strategy Returns')
plt.legend()
plt.show()
