import cv2
import pickle

width, height = 110, 42

try:
    with open('ParkirPos','rb') as f:
        posList = pickle.load(f)

except:
    posList = []

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    with open('ParkirPos','wb') as f:
        pickle.dump(posList,f)

while True:
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    img = cv2.imread('p1.jpeg')
    imgS = cv2.resize(img,(1080, 720))

    for pos in posList:
        cv2.rectangle(imgS,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.imshow("image",imgS)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)