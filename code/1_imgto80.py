import cv2
import matplotlib.pyplot as plt

# 512*512轉成80*80
folder = 'group_3/'
for i in range(0,10000,1):
    filename = str(i)+'.png'

    img = cv2.imread(folder+filename, cv2.IMREAD_GRAYSCALE)
    print(type(img))
    print('shape =' ,img.shape)
    img_re = cv2.resize(img,(80,80), interpolation=cv2.INTER_CUBIC)
    print('re shape = ', img_re.shape)
    cv2.imwrite('./group_3re/'+str(i)+'.png', img_re)
    print('done')