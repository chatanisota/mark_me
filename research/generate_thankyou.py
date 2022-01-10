import numpy as np
import cv2


img = cv2.imread('./thankyou.bmp',0)
img = img.astype(np.float)
img = img/255

print(img.max())
print(img.min())
np.save('./thanyou.npy',img)
