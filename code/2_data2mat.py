# 讀取灰階圖片 將pixel換成0/1 ,接所有結果加入final_data[],輸出成 final_data.mat
import cv2
import matplotlib.pyplot as plt
from scipy.io import savemat
from sklearn.preprocessing import Binarizer
from sklearn import preprocessing
import numpy as np
folder = 'group_3re/'
encoder = Binarizer()
final_data = np.array([])
size=2


for i in range(0,size,1):
    filename = str(i)+'.png'
    img = cv2.imread(folder+filename, cv2.IMREAD_GRAYSCALE)
    np.savetxt('img_0.txt', img)
  
    scaler = preprocessing.StandardScaler().fit(img)
    X_scaled = scaler.transform(img)
    np.savetxt('x_sc.txt',X_scaled)

    encoder.fit(X_scaled)
    img = encoder.transform(X_scaled)

    np.savetxt('img_re.txt', img, fmt='%i')
    final_data = np.append(final_data,img)
  
    print(i,'done')
    
    
print('fin=',final_data)
print(final_data.shape)
final_data = final_data.reshape(size,6400)
print('re_fin= ',final_data)
print(final_data.shape)
savemat('final_data.mat', {'random':final_data})
np.savetxt('final_data.txt', final_data, fmt='%i')