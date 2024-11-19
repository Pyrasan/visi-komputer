import cv2
import numpy as np

# Buka kamera
cap = cv2.VideoCapture(0)  # Ganti '0' dengan path ke kamera jika menggunakan kamera Pi

parking_slots = [
    (100, 100, 200, 200),
    (250, 100, 350, 200),
    (250, 300, 350, 400)
]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Proses gambar untuk deteksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Loop melalui slot parkir dan periksa keberadaan kendaraan
    for slot in parking_slots:
        x1, y1, x2, y2 = slot
        slot_area = thresh[y1:y2, x1:x2]
        non_zero_count = cv2.countNonZero(slot_area)
        
        if non_zero_count > (slot_area.size * 0.5):  # Ambang batas deteksi
            color = (0, 0, 255)  # Merah jika terdeteksi kendaraan
        else:
            color = (0, 255, 0)  # Hijau jika kosong
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    cv2.imshow("Parking Slot Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
