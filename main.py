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
        self.img = None
        self.setupUi(self)
        self.img_original = None
        self.actionAbrir.triggered.connect(self.abrir)
        self.horizontalSlider.valueChanged.connect(self.cambia_brisho)
        self.pushButton.clicked.connect(self.escala_de_grises)
        self.pushButton_2.clicked.connect(self.original)
        self.pushButton_3.clicked.connect(self.negativo)
        self.pushButton_4.clicked.connect(self.rotar_izquierda)
        self.pushButton_5.clicked.connect(self.rotar_derecha)
        self.pushButton_6.clicked.connect(self.espejo_vertical)
    
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
    
    def espejo_vertical(self):
        """Realiza un espejo vertical a la imagen"""
        #img_tmp = self.img[-1::]
        img_tmp = np.flipud(self.img)
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
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
