import cv2
import pickle
import cvzone
import numpy as np

# Load gambar dan resize agar sesuai dengan PemilihParkir.py
image_path = 'p1.jpeg'
img_original = cv2.imread(image_path)
img = cv2.resize(img_original, (1080, 720))

# Load posisi parkir
with open('ParkirPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 110, 42

def checkSlot(imgPro):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        
        # Pastikan koordinat sesuai dimensi gambar yang diresize
        ImgCrop = imgPro[y:y+height, x:x+width]
        count = cv2.countNonZero(ImgCrop)

        # Atur threshold
        if count < 800:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
    
    # Tampilkan jumlah slot parkir yang tersedia
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (50, 50), 
                       scale=2, thickness=3, offset=10, colorR=(0, 200, 0))

# Preprocessing gambar
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     cv2.THRESH_BINARY_INV, 25, 16)
imgMedian = cv2.medianBlur(imgThreshold, 5)
kernel = np.ones((3, 3), np.int8)
imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

# Periksa slot parkir
checkSlot(imgDilate)

# Tampilkan hasil
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()