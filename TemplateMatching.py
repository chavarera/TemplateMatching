import numpy as np
import cv2
import os

def Image(path):
    return cv2.imread(path)

def GrayImage(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def ROI(img):
    return img[216:720, 400:940]

def Canny(img):
    return cv2.Canny(img,100,200)
def match(img,template):
    #print(img,template)
    template = cv2.imread(template, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(GrayImage(img), template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)
    if len(loc[0])>0:
        return True
    else:
        return False
def GetIcons(path):
    return os.listdir(path)
    

def Splited(crop_img):
    all={}
    all['1']=crop_img[0:144,270:540]
    all[2]=crop_img[144:288,270:540]
    all=crop_img[288:432,270:540]
    fourth=crop_img[72:216,0:270]
    fifth=crop_img[216:360,0:270]
    sixth=crop_img[360:504,0:270]
    return fifth

icons=GetIcons('icons/')
img = Image('imgtest.jpg')
gray = GrayImage(img)
roi=ROI(img)

found_data={}
for icon in icons:
    found_data[icon]=match(roi,'icons/'+icon)

print(found_data)
cv2.imshow('mainimage',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
