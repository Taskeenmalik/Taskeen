import pyzbar.pyzbar as pyzbar
import cv2

im=cv2.imread('profile.png')
profile=pyzbar.decode(im)
data=str(profile[0].data)
print(data)
