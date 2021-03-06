# -*- coding: utf-8 -*-
"""final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lPQz6p0IhOBWmbG8j4ZJ3kHVD8Vm5Pvv
"""

import pandas as pd
inputdata = pd.read_csv (r'../data/all_geo.txt',header=None,delimiter=' ')
X=inputdata.drop([6400],axis=1)
Y=pd.read_csv (r'../data/toughness.txt',header=None)

from sklearn.model_selection import train_test_split
Xtrain, Xvalid, Ytrain, Yvalid =train_test_split(X,Y)

from keras import models
from keras import layers
#建構主體為三層fully connection layer
def creat_model():
    inputsize = 6400
    num_classes = 32
    model = models.Sequential()
    model.add(layers.Dense(num_classes,activation='relu', input_shape=(6400,)))
    model.add(layers.Dense(num_classes,activation='relu'))
    model.add(layers.Dense(num_classes,activation='relu'))
    model.add(layers.Dense(1))
    # Compile model
    model.compile(optimizer='rmsprop',loss='mse') #compiler設定，亦嘗試設定為 optimizer = 'adam', loss = 'mean_squared_error'
    return model
model=creat_model()

history = model.fit(X,Y,epochs=250,batch_size=512,validation_data=(X, Y))

#dense_pred = model.predict(Xtest)                    #預測
history_dict = history.history

import matplotlib.pyplot as plt                     #繪製loss曲線
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'b', label='Training loss')       #藍色的是訓練的loss曲線
plt.plot(epochs, val_loss, 'r', label='Validation loss') #紅色的是驗證的loss曲線
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

raw_pred = model.predict(X)
raw_pred_new=pd.DataFrame(raw_pred)
raw_pred_new.columns=['ML']
Y.columns=["Toughness"]
print(model.summary())



output=pd.concat([X,Y,raw_pred_new],axis=1)
output

output.to_csv('dense_result.csv')

# 評估誤差誤差
import numpy as np
def Mape(data_true, data_pred):
  return np.mean(np.abs((data_true - data_pred) / data_true )) * 100
ans=Mape(output['Toughness'],output['ML'])
ans



