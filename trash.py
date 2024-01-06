import cv2
from PIL import Image
import os

fill50k = []
poses = []

for img in os.listdir('./training/fill50k/source'):
    fill50k.append(img)

for img in os.listdir('./training/poses/source'):
    poses.append(img)

for i in range(0,10):
    f5 = cv2.imread('./training/fill50k/source/'+fill50k[i])
    po = cv2.imread('./training/poses/source/'+poses[i])
    a=0