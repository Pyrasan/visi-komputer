# Library yang digunakan

OpenCV | pip install opencv-python

cvzone | pip install cvzone

NumPy | pip install numpy

PyExcel | pip install openpyxl

# Cara Penggunaan

1. Run program PemilihParkir.py dan atur kotak sesuai dengan kotak parkir
2. Run program main.py untuk melihat hasil

Informasi lainnya:
1. Jika ingin mengganti gambar, ubah nama pada `image_path` pada main.py sesuai dengan nama file gambar (dengan format ekstensinya)
2. Untuk mengganti threshold, ubah nilai pada file main.py pada bagian Status slot parkir bagian `if count < x:` sesuai yang diinginkan. Threshold tersebut merupakan nilai piksel yang dideteksi. Jika lebih kecil maka slot parkir dianggap kosong, jika lebih besar dianggap terisi
