from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtWidgets
from ventana_ui import Ui_MainWindow
import cv2 as cv
import numpy as np
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.img = None
        self.img_original = None
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionGuardar.triggered.connect(self.guardar)
        self.horizontalSlider.valueChanged.connect(self.cambia_brisho)
        self.pushButton.clicked.connect(self.escala_de_grises)
        self.pushButton_2.clicked.connect(self.original)
        self.pushButton_3.clicked.connect(self.negativo)
        self.pushButton_4.clicked.connect(self.rotar_izquierda)
        self.pushButton_5.clicked.connect(self.rotar_derecha)
        self.pushButton_6.clicked.connect(self.espejo_horizontal)
        self.pushButton_7.clicked.connect(self.espejo_vertical)
        self.pushButton_8.clicked.connect(self.desenfoque)
        self.pushButton_9.clicked.connect(self.nitidez)
        self.pushButton_10.clicked.connect(self.bordes)
        self.pushButton_11.clicked.connect(self.cartoon)
    
    def original(self):
        if self.img_original is not None:
            self.img = self.img_original
            self.etiqueta.setPixmap(self.convert_cv_qt(self.img)) 
            
    def cambia_brisho(self):
        """Cambia el Brillo de la imagen"""
        valor = np.array([self.horizontalSlider.value()])
        img_tmp = np.clip(self.img + valor,0,255).astype('uint8')
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp 
        

    def escala_de_grises(self):
        """Aplica escala de grises a la imagen"""
        m = np.array([1/3,1/3,1/3])
        img_tmp = np.clip(self.img.dot(m),0,255).astype('uint8')
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp 
        
    def negativo(self):
        """Aplica el negativo a la imagen"""
        img_tmp = 255 - self.img
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp)) 
        self.img = img_tmp 
        
    def rotar_izquierda(self):
        """Rota la imagen 90 grados a la izquierda con una funcion de numpy"""
        img_tmp = np.rot90(self.img)
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))    
        self.img = img_tmp 

    def rotar_derecha(self):
        """Rota la imagen 90 grados a la derecha con una funcion de numpy"""
        img_tmp = np.rot90(self.img,k=3)
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp 
    
    def espejo_horizontal(self):
        """Realiza un espejo horitzontal a la imagen"""
        img_tmp = self.img[::-1,:]
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp
    
    def espejo_vertical(self):
        """Realiza un espejo vertical a la imagen"""
        img_tmp = self.img[:,::-1]
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp
        
    def desenfoque(self):
        """Realiza el desenfoque con la matriz blur Gaussiana"""
        blur = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]]) 
        blur = (1/256)*blur
        img_tmp = cv.filter2D(self.img, -1,blur)
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp
        
    def nitidez(self):
        """Realiza el desenfoque con la matriz unsharp"""
        unsharp = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,-476,24,6],[4,16,24,16,4],[1,4,6,4,1]]) 
        unsharp = (-1/256)*unsharp
        img_tmp = cv.filter2D(self.img, -1,unsharp)
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp
    
    def bordes(self):
        """Se obtienen los bordes de la imagen"""
        img_act = self.img
        sobel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        sobel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        gx = cv.filter2D(img_act, -1, sobel_x)
        gy = cv.filter2D(img_act, -1, sobel_y)
        img_tmp = np.abs(gx) + np.abs(gy)
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp
        
    def cartoon(self):
        """Efecto que me dio claude"""
        kernel = np.array([[-4, -2, 0],
                    [-2,  1, 2],
                    [ 0,  2, 4]], np.float32) 
            
        img_tmp = cv.filter2D(self.img, -1,kernel)
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        self.img = img_tmp
        
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        converted_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(converted_image)
    
    def abrir(self):
        archi = QFileDialog(self)
        
        file, _ = archi.getOpenFileName(self, "Selecciona una imagen", "", "Imagenes *.jpg *.png *.bmp *.jpeg")
        
        if file:
            imagen = QPixmap(file)
            self.etiqueta.setPixmap(imagen)
            self.img = cv.imread(file)
            self.img_original = cv.imread(file)
        
    def guardar(self):
        """Ya guarda la imagen editada"""
        if self.img is not None:
            archi = QFileDialog(self)
            
            ruta_archivo, _ = archi.getSaveFileName(
                        self,
                        "Guardar imagen",
                        "imagen_guardada.png",
                        "Imágenes PNG (*.png);;Imágenes JPEG (*.jpg *.jpeg);;Todos los archivos (*)"
                        )

            if ruta_archivo:
                self.etiqueta.pixmap().save(ruta_archivo)

        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
