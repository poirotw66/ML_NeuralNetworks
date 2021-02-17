from google.colab import drive
drive.mount('/content/gdrive')
import pandas as pd
import numpy as np
data = pd.read_table('/content/gdrive/My Drive/ML_Final/all_geo.txt',header=None,encoding='gb2312',sep=' ')
print(data.shape)
data_0=data.iloc[:,:-1]
print(data_0.shape)

toug = pd.read_table('/content/gdrive/My Drive/ML_Final/toughness.txt',header=None,encoding='gb2312')
traindata=np.column_stack((data_0,toug))
traindata_pd = pd.DataFrame(data=traindata)
traindata_pd.to_csv('Fin_train.csv',index=0)
traindata_pd=traindata_pd.rename(columns={traindata_pd.columns[6400]:'Toughness'},inplace=True)