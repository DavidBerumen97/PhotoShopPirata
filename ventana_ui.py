# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(869, 630)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 641, 61))
        font = QFont()
        font.setFamilies([u"Mi Letra Fea"])
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta = QLabel(self.centralwidget)
        self.etiqueta.setObjectName(u"etiqueta")
        self.etiqueta.setGeometry(QRect(60, 100, 411, 291))
        self.etiqueta.setFrameShape(QFrame.Shape.Box)
        self.etiqueta.setFrameShadow(QFrame.Shadow.Plain)
        self.etiqueta.setScaledContents(True)
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(70, 410, 361, 25))
        self.horizontalSlider.setMinimum(-255)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 440, 58, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 90, 131, 34))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 500, 131, 34))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(700, 90, 88, 34))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(680, 210, 121, 34))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(500, 210, 131, 34))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(510, 280, 121, 34))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(670, 280, 141, 34))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(520, 150, 88, 34))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(700, 140, 88, 34))
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(520, 350, 88, 34))
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(690, 350, 88, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 869, 30))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PhotoPirata", None))
        self.etiqueta.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Brillo", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Escala de Grises", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Volver a Original", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Negativo", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Rotar Izquierda", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Rotar Derecha", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Espejo Horizontal", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Espejo Vertical", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Desenfoque", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Nitidez", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Bordes", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Kernel", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

