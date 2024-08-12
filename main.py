# Generales #############################################################

import os
import sys

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import time
import numpy as np
import os.path
from os import path
from datetime import datetime, timedelta
import subprocess

# Interfaz Grafica ######################################################


import PyQt5.QtCore as QtCore

# from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtTest, QtCore

from pygame import mixer  # Load the popular external library

import numpy as np
import mediapipe as mp

import pandas as pd

from datetime import datetime
import matplotlib.pyplot as plt

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import socket
import struct
from keras.models import load_model
import threading
import serial.tools.list_ports
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
from collections import deque

from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QPainter, QColor, QFont, QPen

# FECHA
ahora = datetime.now()
dateNOW = ahora.strftime("%Y-%m-%d %H:%M:%S")


"""
      *************    # CLASES A ENTRENAR (CSV) ***************************
"""

totalClases = 84

"""
      *************    REGISTRO PDF APP ***************************
"""
directorioReportes = "./registros/"
tiempoInforme = 12

"""
      *************    EFECTOS SONIDO  APP ***************************
"""
# sonidoMouseMove  = 'guide/sonidos/hover.mp3'
sonidoMouseClick = "guide/sonidos/click.mp3"
sonidoNotificacion = "guide/sonidos/notificacion.mp3"
sonidoMouseMove = "guide/sonidos/cursor-move.mp3"
# sonidoMouseClick = 'guide/sonidos/cursor-select.mp3'


"""
      *************    ESTILOS APP ***************************
"""

estiloBtnPresionado_Blue = """QWidget { 
                background-color:#3c4454; 
                color: white;
                font: 8pt "MS Shell Dlg 2";
                border-radius: 12px;
                border: 0px solid transparent;
                border-left: 3px solid #568af2;}"""

estiloBtnPresionado_Verde = """
                QWidget { 
                background-color:#3c4454; 
                color: white;
                font: 8pt "MS Shell Dlg 2";
                border-radius: 12px;
                border: 0px solid transparent;
                border-left: 3px solid green;}"""

estiloBtnPresionado_Verde2 = """
                QWidget { 
                background-color: #494E58; 
                color: white;
                font: 10pt "MS Shell Dlg 2";
                border-radius: 12px;
                border: 0px solid transparent;
                border-left: 5px solid green;
                border-right: 5px solid green;
                }"""

estiloBtnPresionado_Capturar = """
                QWidget { 
                background-color: #494E58; 
                color: white;
                font: 10pt "MS Shell Dlg 2";
                border-radius: 12px;
                border: 0px solid transparent;
                border-left: 5px solid #BEB728;
                border-right: 5px solid #BEB728;
                }"""

estiloHoverGris = """
                QWidget { 
                background-color: #3c4454;
                
                color: white;
                font: 800 9pt "Segoe UI";
                }"""

estiloHoverAzul = """
                QWidget { 
                background-color: #568af2;
                
                color: white;
                font: 800 9pt "Segoe UI";
                 }"""

estiloHoverBlanco = """
                QWidget { 
                background-color: #fff;
                
                color: #000;
                font: 400 9pt "Segoe UI";
                border-radius: 4px;
                border: 3px solid #568af2;               
                 }"""

estiloHoverEscala = """
                QWidget { 
                background-color: #2c313c;
                
                color: #ffffff;
                border: 2px solid #ffffff;               
                 }"""

estiloHoverMuestras = """
                QWidget { 
                background-color: #3c4454;               
                color: #fff;
                font: 500 16pt "Segoe UI";
                border-radius: 4px;
                border: 3px solid #568af2;               
                 }"""

estiloHoverVerde = """
                QWidget { 
                background-color: #3EAC30;
                
                color: white;
                font: 800 9pt "Segoe UI";
                 }"""

estiloSinBordeIzquierdo = """
                 QWidget { 
                 border-left: 0px; }"""

estiloBtnNormal = """
                QWidget { 
                background-color: #1b1e23; 
                font: 8pt "MS Shell Dlg 2";}"""

estiloBtnNormal2 = """
                QWidget { 
                    
                color: white;
                background-color: #1b1e23; 
                font: 10pt "MS Shell Dlg 2";}"""

estiloTooltip = """
                QToolTip { 
                background-color: #1b1e23; 
                color: #8a95aa;
                padding-left: 10px;
                padding-right: 10px;
                border-radius: 8px;
                border: 0px solid transparent;
                border-left: 3px solid #568af2;
                font: 800 9pt "Segoe UI";
                min-width: 120px;
                max-width: 120%; 
                 }"""

estiloBtnSalir = """
                QWidget { 
                background-color: red;
                color: white;
                }
             
             
                QToolTip { 
                background-color: #1b1e23; 
                color: #8a95aa;
                padding-left: 10px;
                padding-right: 10px;
                border-radius: 8px;
                border: 0px solid transparent;
                border-left: 3px solid #568af2;
                font: 800 9pt "Segoe UI";
                min-width: 50px;
                max-width: 50%; 
                }"""

estiloBtnMaximizar = """
                                            
                 QWidget { 
                  background-color: #BEB728;
                  color: white;
                  }
                 
                 
                  QToolTip { 
                background-color: #1b1e23; 
                color: #8a95aa;
                padding-left: 10px;
                padding-right: 10px;
                border-radius: 8px;
                border: 0px solid transparent;
                border-left: 3px solid #568af2;
                font: 800 9pt "Segoe UI";
                min-width: 90px;
                max-width: 90%; }"""

estiloBtnMinimizar = """
                
                QWidget { 
                     background-color: green; 
                     color: white;
                      }
                
                QToolTip { 
                   background-color: #1b1e23; 
                   color: #8a95aa;
                   padding-left: 10px;
                   padding-right: 10px;
                   border-radius: 8px;
                   border: 0px solid transparent;
                   border-left: 3px solid #568af2;
                   font: 800 9pt "Segoe UI";
                   min-width: 90px;
                   max-width: 90%; 
                    }"""

estiloBtnControl = """QWidget { 
                    background-color: #343b48; 
                    color: white;
                  
                     }"""

estiloTooltip100 = """QToolTip { 
                    background-color: #1b1e23; 
                    color: #8a95aa;
                    padding-left: 10px;
                    padding-right: 10px;
                    border-radius: 8px;
                    border: 0px solid transparent;
                    border-left: 3px solid #568af2;
                    font: 800 9pt "Segoe UI";
                    min-width: 100px;
                    max-width: 90%; 
                     }"""

estiloTooltip70 = """QToolTip { 
                    background-color: #1b1e23; 
                    color: #8a95aa;
                    padding-left: 10px;
                    padding-right: 10px;
                    border-radius: 8px;
                    border: 0px solid transparent;
                    border-left: 3px solid #568af2;
                    font: 800 9pt "Segoe UI";
                    min-width: 70px;
                    max-width: 70%; 
                     }"""

estiloBtnCamaraON = """                                        
                    QWidget { 
                    background-color: #3EAC30;
                    color: white;
                    font: 800 10pt "Segoe UI";
                    }
                    """

estiloBtnCamaraOFF = """                                        
                    QWidget { 
                    background-color: red;
                    color: white;
                    font: 800 10pt "Segoe UI";
                    }
                    """

estiloBtnHoverAmarillo = """
                                            
                    QWidget { 
                    background-color: #BEB728;
                    
                    color: white;
                    font: 800 10pt "Segoe UI";
                    }
                    """

estiloBtnHoverAzul2 = """
                                            
                    QWidget { 
                    background-color: #568af2;
                    
                    color: white;
                    font: 800 14pt "Segoe UI";
                    }
                    """

estiloTextoLista = """
                QWidget {      
                color: white;
                font: 14pt "Berlin Sans FB";
                
                 }"""

estiloTextoFecha = """
                QWidget {      
                color: white;
                font-size:10pt; font-style:italic;
                 }"""

estiloTextoFecha2 = """
                QWidget {      
                color: white;
                font-size:13pt; font-style:italic;
                 }"""

estiloAzulLista = """
                QWidget { 
                background-color: #568af2;
                
                color: white;
                
                 }"""

estiloNotificacionDescripcion = """
                QWidget { 
               
                background-color: #FFFAF0E6;
                color:#000;                
                font: 10pt "MS Shell Dlg 2";font-style:italic;                        
                }"""

estiloFondoNotificacion = """
                QWidget { 
                            
background-color: #FFFAF0E6;
    
         border-radius:15px solid #000;     

                            
                 }"""

estiloNotificacionNombre = """
                QWidget { 
                            
                    font: 14pt "Berlin Sans FB";
                    color: #000;
                    font: 800 14pt "Segoe UI";

                            
                 }"""


estiloAmarillo = """
                QWidget {         
                background-color:#fdcd34;
                color: #ffffff;
                }"""
estiloGris = """
                QWidget {         
                background-color:#838485;
                color: #ffffff;
                }"""

estiloAlerta = """
                QWidget {         
                background-color:#838485;
                color: #ffffff;
                }"""

estiloCuenta = """
                QWidget { 
             
                   color: white;
                   font: 24pt "MS Shell Dlg 2";
                    }
                """

estiloGrafica = """
                QWidget {         
                background-color:#2c313c;
                color: #ffffff;
                }"""

ser = None
dataY = deque(maxlen=4000)
collecting_data = False
collected_data = []
collected_data2 = []
continuarProceso = False
collecting_data2 = False
data_count = 0


def send_data(data):
    host = "localhost"
    port = 12345
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(data.encode())
            print(f"Data sent: {data}")
    except ConnectionRefusedError:
        print("Failed to connect to the server. Ensure the server is running.")


def connect_sensor(port, baudrate):
    global ser

    try:
        ser = serial.Serial(port, int(baudrate), timeout=1)
        print("PUERTO ABIERTO")

        data_thread = threading.Thread(target=ventanaGraficas().read_data)
        data_thread.daemon = True
        data_thread.start()

    except Exception as e:

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("El dispositivo no disponible: " + str(e))
        msg.exec_()


def disconnect_sensor():
    global ser
    if ser:
        ser.close()
        ser = None


class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estabilizando sensor")
        self.setFixedSize(300, 80)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Crear etiqueta de mensaje
        self.label = QLabel("Estabilizando sensor...", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Crear barra de progreso
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.progress_bar)

        # Temporizador para la barra de progreso
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)

        # Inicializar el valor de la barra de progreso
        self.progress_value = 0

    def startProgress(self):
        self.progress_value = 0
        self.progress_bar.setValue(self.progress_value)

        # Iniciar temporizador para simular la carga
        self.timer.start(100)  # Cada 100 ms actualiza la barra

        # Temporizador para cerrar el diálogo después de 10 segundos
        QTimer.singleShot(10000, self.finishProgress)

    def updateProgress(self):
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer.stop()

    def finishProgress(self):
        self.timer.stop()
        self.accept()  # Cerrar el cuadro de diálogo


class CircularProgress(QWidget):
    def __init__(self, line_thickness=10):
        super().__init__()
        self.value = 0
        self.line_thickness = line_thickness
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(20)  # Ajusta la velocidad del progreso

    def update_progress(self):
        if self.value < 100:
            self.value += 1
        else:
            self.timer.stop()

        self.update()

    def get_color(self):
        # De rojo a verde
        red = int(255 * (1 - self.value / 100))
        green = int(255 * (self.value / 100))
        return QColor(red, green, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(0, 0, self.width(), self.height())
        painter.setRenderHint(QPainter.Antialiasing)

        # Fondo
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(240, 240, 240))
        painter.drawEllipse(rect)

        # Arco de progreso (estático)
        painter.setBrush(Qt.NoBrush)
        pen = QPen(QColor(200, 200, 200))
        pen.setWidth(self.line_thickness)
        painter.setPen(pen)
        painter.drawEllipse(
            rect.adjusted(
                self.line_thickness // 2,
                self.line_thickness // 2,
                -self.line_thickness // 2,
                -self.line_thickness // 2,
            )
        )

        # Arco dinámico (progreso)
        color = self.get_color()
        pen.setColor(QColor(color))
        painter.setPen(pen)
        start_angle = 90 * 16
        span_angle = -int(
            self.value * 360 * 16 / 100
        )  # Asegurarse de que span_angle sea un entero
        painter.drawArc(
            rect.adjusted(
                self.line_thickness // 2,
                self.line_thickness // 2,
                -self.line_thickness // 2,
                -self.line_thickness // 2,
            ),
            start_angle,
            span_angle,
        )

        # Texto
        painter.setPen(QColor(50, 50, 50))
        painter.setFont(QFont("Arial", 20))
        painter.drawText(rect, Qt.AlignCenter, f"{self.value}%")


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class ventanaPrincipal(QMainWindow):

    def __init__(self):
        super(ventanaPrincipal, self).__init__()

        self.ui = loadUi("guide/ventanas/main.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(180)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(60, 192, 157, 550))
        self.setGraphicsEffect(self.shadow)

        self.btnMenuLateral.setIcon(QtGui.QIcon("guide/iconos/icon_menu_close.svg"))

        # self.centrarVentana()

        self.frameInicio.installEventFilter(self)
        self.frameEntrenador.installEventFilter(self)
        self.frameAnalisis.installEventFilter(self)
        self.frameRegistros.installEventFilter(self)
        self.btnAcerca.installEventFilter(self)
        self.btnExit.installEventFilter(self)
        self.btnMaximizar.installEventFilter(self)
        self.btnMinimizar.installEventFilter(self)
        self.frameLateral.installEventFilter(self)

        self.boolInicio = False
        self.boolEntrenador = False
        self.boolAnalisis = False
        self.boolRegistros = False
        self.boolAcerca = False

        self.frame1 = ventanaInicio()
        self.frame2 = ventanaControl()
        self.frame3 = ventanaAdquisicion()
        self.frame4 = ventanaGraficas()
        self.frame5 = ventanaAcerca()

        self.ventanas = QtWidgets.QStackedWidget(self.ventanas)

        self.ventanas.addWidget(self.frame1)
        self.ventanas.addWidget(self.frame2)
        self.ventanas.addWidget(self.frame3)
        self.ventanas.addWidget(self.frame4)
        self.ventanas.addWidget(self.frame5)

        # self.ventanas.setFixedHeight(713)
        # self.ventanas.setFixedWidth(1240)

        self.ventanas.setFixedHeight(588)
        self.ventanas.setFixedWidth(941)

        # self.ventanas.setCurrentIndex(0)

        self.funcionInicio()

        # self.containerNotificacion =  self.funcionBloqueNotificacion('guide/iconos/error.png',"Método Ergonómico Necesario","Seleccionar un método para el análisis")

        def setupUi(self, ventanaPrincipal):
            pass

        def moveWindow(e):

            if self.isMaximized() == False:

                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.header.mouseMoveEvent = moveWindow

        self.btnExit.clicked.connect(self.funcionSalirApp)
        self.btnMaximizar.clicked.connect(
            lambda: (self.restore_or_maximize_window(), self.tonoClick())
        )
        self.btnMinimizar.clicked.connect(
            lambda: (self.showMinimized(), self.tonoClick())
        )
        self.btnMenuLateral.clicked.connect(lambda: self.mostrar_ocultar_menuLateral())

        self.btnInicio.clicked.connect(self.funcionInicio)
        self.btnEntrenador.clicked.connect(self.funcionEntrenador)
        self.btnAnalisis.clicked.connect(self.funcionAnalisis)
        self.btnRegistros.clicked.connect(self.funcionRegistros)
        self.btnAcerca.clicked.connect(self.funcionAcerca)

        self.btnEntrenador.setEnabled(False)
        self.btnAnalisis.setEnabled(False)
        self.btnRegistros.setEnabled(False)

        listaUSB = list()
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            print(p)

            # print(p.device)

            # if "Dispositivo serie USB" in p.description:
            listaUSB.append(p.device)
        self.comboPuertos.clear()
        self.comboPuertos.addItems(listaUSB)

        self.estadoConexion = False

        # CircularProgress(line_thickness=20)  # Ajusta el grosor de la línea aquí

    def fcnHabilitar(self):
        self.btnEntrenador.setEnabled(True)
        self.btnAnalisis.setEnabled(True)
        self.btnRegistros.setEnabled(True)

    def fcnDeshabilitar(self):
        self.btnEntrenador.setEnabled(False)
        self.btnAnalisis.setEnabled(False)
        self.btnRegistros.setEnabled(False)

    def showProgressDialog(self):
        dialog = ProgressDialog()
        dialog.startProgress()
        dialog.exec_()

    def centrarVentana(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def funcionSalirApp(self):

        self.tonoClick()
        self.close()

    def funcionInicio(self):

        global continuarProceso

        continuarProceso = False
        self.frame2.apagar()

        self.tonoClick()

        """
        if(self.frame2.ON):
            self.frame2.ON=False
            self.frame2.detenerVideo()
                   
        if(self.frame3.ON):
            self.frame3.ON=False
            self.frame3.detenerVideo()
        """

        self.ventanas.setCurrentIndex(0)

        if self.boolInicio == False:
            self.frameInicio.setStyleSheet(estiloBtnPresionado_Blue)
            self.btnInicio.setStyleSheet(estiloSinBordeIzquierdo)

            self.boolInicio = True
            self.boolRegistros = False
            self.boolEntrenador = False
            self.boolAnalisis = False
            self.boolAcerca = False

            self.frameEntrenador.setStyleSheet(estiloBtnNormal)
            self.frameAnalisis.setStyleSheet(estiloBtnNormal)
            # self.frameAcerca.setStyleSheet(estiloBtnNormal)
            self.frameRegistros.setStyleSheet(estiloBtnNormal)

    def funcionEntrenador(self):

        self.tonoClick()
        self.frame2.apagar()

        """
        if(self.frame2.ON):
            self.frame2.ON=False
            self.frame2.detenerVideo()
        """

        if self.frame3.ON:
            self.frame3.ON = False
            self.frame3.detenerVideo()

        self.ventanas.setCurrentIndex(1)

        if self.boolEntrenador == False:
            self.frameEntrenador.setStyleSheet(estiloBtnPresionado_Blue)
            self.btnEntrenador.setStyleSheet(estiloSinBordeIzquierdo)

            self.boolEntrenador = True
            self.boolInicio = False
            self.boolRegistros = False
            self.boolAnalisis = False
            self.boolAcerca = False

            self.frameInicio.setStyleSheet(estiloBtnNormal)
            self.frameAnalisis.setStyleSheet(estiloBtnNormal)
            self.frameAcerca.setStyleSheet(estiloBtnNormal)
            self.frameRegistros.setStyleSheet(estiloBtnNormal)

    def funcionAnalisis(self):

        global continuarProceso

        continuarProceso = False
        self.frame2.apagar()

        self.tonoClick()

        """    
        
        if(self.frame3.ON):
            self.frame3.ON=False
            self.frame3.detenerVideo()
        
        """
        self.ventanas.setCurrentIndex(2)

        if self.boolAnalisis == False:
            self.frameAnalisis.setStyleSheet(estiloBtnPresionado_Blue)
            self.btnAnalisis.setStyleSheet(estiloSinBordeIzquierdo)

            self.boolAnalisis = True
            self.boolInicio = False
            self.boolEntrenador = False
            self.boolRegistros = False
            self.boolAcerca = False

            self.frameInicio.setStyleSheet(estiloBtnNormal)
            self.frameEntrenador.setStyleSheet(estiloBtnNormal)
            self.frameAcerca.setStyleSheet(estiloBtnNormal)
            self.frameRegistros.setStyleSheet(estiloBtnNormal)

    def funcionRegistros(self):

        global continuarProceso

        continuarProceso = False
        self.frame2.apagar()
        """ 

        if(self.frame2.ON):
            self.frame2.ON=False
            self.frame2.detenerVideo()


        if(self.frame3.ON):
            self.frame3.ON=False
            self.frame3.detenerVideo()

        """

        self.tonoClick()
        # if (self.frame4.widgetLista.count() > 0):
        # self.frame4.widgetLista.clear()
        # self.frame4.agregarItems()

        # print(self.frame4.widgetLista.count())

        self.ventanas.setCurrentIndex(3)

        if self.boolRegistros == False:
            self.frameRegistros.setStyleSheet(estiloBtnPresionado_Blue)
            self.btnRegistros.setStyleSheet(estiloSinBordeIzquierdo)

            self.boolRegistros = True
            self.boolInicio = False
            self.boolEntrenador = False
            self.boolAnalisis = False
            self.boolAcerca = False

            self.frameInicio.setStyleSheet(estiloBtnNormal)
            self.frameEntrenador.setStyleSheet(estiloBtnNormal)
            self.frameAnalisis.setStyleSheet(estiloBtnNormal)
            self.frameAcerca.setStyleSheet(estiloBtnNormal)

    def funcionAcerca(self):
        global ser
        self.tonoClick()

        if self.estadoConexion == False:
            connect_sensor(
                self.comboPuertos.currentText(), self.comboVelocidad.currentText()
            )

            if ser.is_open:
                imgW = "guide/imagenes/ON.png"
                self.btnAcerca.setIcon(QtGui.QIcon(imgW))
                self.btnAcerca.setText("     DESCONECTAR")

                
                cntEnable = 0
                self.progreso.addWidget(CircularProgress(line_thickness=20))

                for index in range(10):
                    cntEnable += 1
                    QtTest.QTest.qWait(1000)
                    if cntEnable == 10:
                        self.fcnHabilitar()
                        self.estadoConexion = True


        # self.showProgressDialog()

        else:
            disconnect_sensor()
            self.estadoConexion = False
            imgW = "guide/imagenes/OFF.png"
            self.btnAcerca.setIcon(QtGui.QIcon(imgW))
            self.btnAcerca.setText("     CONECTAR")
            self.fcnDeshabilitar()
            # self.progreso.setVisible(False)

    def tonoMenu(self):
        mixer.init()
        mixer.music.load(sonidoMouseMove)
        mixer.music.play()

    def tonoClick(self):

        mixer.init()
        mixer.music.load(sonidoMouseClick)
        mixer.music.play()

    def eventFilter(self, object, event):

        if object is self.frameLateral and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.frameLateral.setStyleSheet(estiloHoverGris)

            return True

        elif object is self.frameLateral and event.type() == QtCore.QEvent.Leave:

            self.frameLateral.setStyleSheet(estiloBtnNormal)

        if object is self.frameInicio and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.frameInicio.setStyleSheet(estiloHoverAzul)

            return True

        elif object is self.frameInicio and event.type() == QtCore.QEvent.Leave:

            if self.boolInicio == False:
                self.frameInicio.setStyleSheet(estiloBtnNormal)

            else:
                self.frameInicio.setStyleSheet(estiloBtnPresionado_Blue)

        if self.estadoConexion:
            if object is self.frameEntrenador and event.type() == QtCore.QEvent.Enter:

                self.tonoMenu()
                self.frameEntrenador.setStyleSheet(estiloHoverAzul)

                return True

            elif object is self.frameEntrenador and event.type() == QtCore.QEvent.Leave:

                if self.boolEntrenador == False:
                    self.frameEntrenador.setStyleSheet(estiloBtnNormal)

                else:
                    self.frameEntrenador.setStyleSheet(estiloBtnPresionado_Blue)

            if object is self.frameAnalisis and event.type() == QtCore.QEvent.Enter:

                self.tonoMenu()
                self.frameAnalisis.setStyleSheet(estiloHoverAzul)

                return True

            elif object is self.frameAnalisis and event.type() == QtCore.QEvent.Leave:

                if self.boolAnalisis == False:
                    self.frameAnalisis.setStyleSheet(estiloBtnNormal)

                else:
                    self.frameAnalisis.setStyleSheet(estiloBtnPresionado_Blue)

            if object is self.frameRegistros and event.type() == QtCore.QEvent.Enter:

                self.tonoMenu()
                self.frameRegistros.setStyleSheet(estiloHoverAzul)

                return True

            elif object is self.frameRegistros and event.type() == QtCore.QEvent.Leave:

                if self.boolRegistros == False:
                    self.frameRegistros.setStyleSheet(estiloBtnNormal)

                else:
                    self.frameRegistros.setStyleSheet(estiloBtnPresionado_Blue)

        if object is self.btnAcerca and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnAcerca.setStyleSheet(estiloHoverVerde)

            return True

        elif object is self.btnAcerca and event.type() == QtCore.QEvent.Leave:

            if self.boolAcerca == False:
                self.btnAcerca.setStyleSheet(estiloBtnNormal)

            else:
                self.btnAcerca.setStyleSheet(estiloBtnPresionado_Verde)

        if object is self.btnExit and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnExit.setStyleSheet(estiloBtnSalir)
            self.btnExit.setToolTip("Salir")

            return True

        elif object is self.btnExit and event.type() == QtCore.QEvent.Leave:

            self.btnExit.setStyleSheet(estiloBtnControl)

        if object is self.btnMaximizar and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnMaximizar.setStyleSheet(estiloBtnMaximizar)
            self.btnMaximizar.setToolTip("Maximizar")

            return True

        elif object is self.btnMaximizar and event.type() == QtCore.QEvent.Leave:

            self.btnMaximizar.setStyleSheet(estiloBtnControl)

        if object is self.btnMinimizar and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnMinimizar.setStyleSheet(estiloBtnMinimizar)
            self.btnMinimizar.setToolTip("Minimizar")

            return True

        elif object is self.btnMinimizar and event.type() == QtCore.QEvent.Leave:

            self.btnMinimizar.setStyleSheet(estiloBtnControl)

        return False

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):

        if self.isMaximized():
            self.showNormal()

            # width = self.frameGeometry().width()
            # height = self.frameGeometry().height()

            # nuevoAnchoFrames=width-1240
            # nuevoAltoFrames=height-713

            # print(nuevoAnchoFrames)
            # print(nuevoAltoFrames)

            # self.ventanas.setFixedHeight(713)
            # self.ventanas.setFixedWidth(1240)
            self.ventanas.setFixedHeight(563)
            self.ventanas.setFixedWidth(941)

        else:
            self.showMaximized()

            width = self.frameGeometry().width()
            height = self.frameGeometry().height()

            width = width - 260
            height = height - 137

            self.ventanas.setFixedHeight(height)
            self.ventanas.setFixedWidth(width)

            # print(width)
            # print(height)

    def mostrar_ocultar_menuLateral(self):

        ancho = self.slider_menu_container.width()

        self.tonoClick()

        if ancho == 50:
            self.btnMenuLateral.setIcon(QtGui.QIcon("guide/iconos/icon_menu_close.svg"))

            nuevoAncho = 200

            self.btnInicio.setToolTip(None)
            self.btnEntrenador.setToolTip(None)
            self.btnAnalisis.setToolTip(None)
            self.btnRegistros.setToolTip(None)
            self.btnAcerca.setToolTip(None)
            self.btnMenuLateral.setToolTip(None)
            self.frameAcerca.setVisible(True)

        else:

            self.btnMenuLateral.setIcon(QtGui.QIcon("guide/iconos/icon_menu.svg"))

            nuevoAncho = 50

            self.btnMenuLateral.setStyleSheet(estiloTooltip)
            self.btnMenuLateral.setToolTip("Mostrar Menú")

            self.btnInicio.setStyleSheet(estiloTooltip70)
            self.btnInicio.setToolTip("Inicio")
            self.btnInicio.setStyleSheet(estiloSinBordeIzquierdo)

            self.btnEntrenador.setStyleSheet(estiloTooltip100)
            self.btnEntrenador.setToolTip("Ventana Control")
            self.btnEntrenador.setStyleSheet(estiloSinBordeIzquierdo)

            self.btnAnalisis.setStyleSheet(estiloTooltip70)
            self.btnAnalisis.setToolTip("Ventana Adquisión")
            self.btnAnalisis.setStyleSheet(estiloSinBordeIzquierdo)

            self.btnRegistros.setStyleSheet(estiloTooltip100)
            self.btnRegistros.setToolTip("Ventana Gráficas")
            self.btnRegistros.setStyleSheet(estiloSinBordeIzquierdo)

            self.frameAcerca.setVisible(False)

        self.animation = QPropertyAnimation(self.slider_menu_container, b"maximumWidth")

        self.animation.setDuration(450)
        self.animation.setStartValue(ancho)
        self.animation.setEndValue(nuevoAncho)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


class ventanaInicio(QFrame):
    def __init__(self):
        super(ventanaInicio, self).__init__()
        loadUi("guide/ventanas/inicio.ui", self)

        self.labelInstrucciones.setVisible(False)

        self.movie = QMovie("guide/imagenes/main.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.btnInstrucciones.installEventFilter(self)

        self.instruccion = False
        self.btnInstrucciones.clicked.connect(self.estadoInstruccion)
        self.label.setVisible(True)
        self.labelInstrucciones.setVisible(False)

    def estadoInstruccion(self):
        self.tonoClick()

        if self.instruccion == False:
            self.instruccion = True
            self.btnInstrucciones.setText("OCULTAR")
            self.label.setVisible(False)
            self.labelInstrucciones.setVisible(True)

        else:
            self.instruccion = False
            self.btnInstrucciones.setText("INSTRUCCIONES")
            self.label.setVisible(True)
            self.labelInstrucciones.setVisible(False)

    def eventFilter(self, object, event):

        if object is self.btnInstrucciones and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnInstrucciones.setStyleSheet(estiloBtnHoverAzul2)

            return True

        elif object is self.btnInstrucciones and event.type() == QtCore.QEvent.Leave:

            self.btnInstrucciones.setStyleSheet(
                """QWidget { 
                   background-color: #1b1e23;  
                   color: white;
                   font: 12pt "MS Shell Dlg 2";
                    }"""
            )
        return False

    def tonoMenu(self):
        mixer.init()
        mixer.music.load(sonidoMouseMove)
        mixer.music.play()

    def tonoClick(self):
        mixer.init()
        mixer.music.load(sonidoMouseClick)
        mixer.music.play()


class ventanaControl(QFrame):
    def __init__(self):

        super(ventanaControl, self).__init__()
        loadUi("guide/ventanas/control.ui", self)

        self.btnIniciar.installEventFilter(self)

        self.lblAnalizar.setVisible(False)
        self.lblAnalizar.setStyleSheet(estiloBtnNormal2)

        self.serial_connection = None
        self.reading_thread = None
        self.stop_thread = threading.Event()

        self.collected_data = []
        self.data_count = 0
        self.start_time = None
        self.model = load_model("modelo/CNNREFORZADA.h5")
        self.previous_movement = None  # Initialize previous_movement here

        self.btnIniciar.clicked.connect(self.encender)
        self.btnSTOP.clicked.connect(self.apagar)

        pixmap = QPixmap("guide/imagenes/checked.png")
        self.imgEstado.setPixmap(pixmap)
        self.lblResultado.setText("")

        self.imgEstado.setVisible(False)

        self.estadoRecoleccion = False

        self.movie = QMovie("guide/imagenes/cerebro2.gif")
        self.lblGif1.setMovie(self.movie)
        self.movie.start()
        self.apagar()

    def apagar(self):
        self.tonoClick()
        global continuarProceso

        continuarProceso = False
        self.stop_collecting_data()

        self.lblAnalizar.setVisible(False)

        self.estadoRecoleccion = False

        collected_data = []
        collecting_data = False

        self.btnIniciar.setText("INICIAR")

        self.frame1.setStyleSheet(estiloGris)
        self.frame2.setStyleSheet(estiloGris)
        self.frame3.setStyleSheet(estiloGris)
        self.frame4.setStyleSheet(estiloGris)
        self.frame5.setStyleSheet(estiloGris)
        self.frame6.setStyleSheet(estiloGris)

        pixmap = QPixmap("guide/imagenes/OFF.png")
        self.lblListo.setPixmap(pixmap)

    def encender(self):
        self.tonoClick()
        global continuarProceso
        continuarProceso = True
        self.start_collecting_data()

    def start_collecting_data(self):

        global collecting_data, collected_data, continuarProceso

        self.lblAnalizar.setVisible(True)

        # self.estadoRecoleccion = False

        collected_data = []
        collecting_data = True
        # self.update_circle(self.collecting_label, "green")
        pixmap = QPixmap("guide/imagenes/ON.png")
        self.lblListo.setPixmap(pixmap)

        self.collected_data = []
        self.data_count = 0
        self.start_time = time.time()
        collect_time = int(self.editCuenta.toPlainText())

        print(f"Recolección de datos iniciada por {collect_time} segundos.")
        QTimer.singleShot(collect_time * 1000, self.stop_collecting_data)

        for index in range(collect_time):
            print("conteo: ", index)
            self.lblAnalizar.setText(
                "Analizando...  " + str(index + 1) + "/" + self.editCuenta.toPlainText()
            )
            if continuarProceso == False:
                break
            QtTest.QTest.qWait(1000)

    def stop_collecting_data(self):
        global collecting_data
        collecting_data = False
        pixmap = QPixmap("guide/imagenes/OFF.png")
        self.lblListo.setPixmap(pixmap)
        print(f"Recolección detenida. {len(self.collected_data)} datos recolectados.")
        self.process_data()

        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Mensaje")
        msg.setText("Análisis terminado")
        msg.exec_()
        """

    def process_data(self):
        global collected_data, collecting_data, continuarProceso
        print("datooooooooo: ", len(collected_data))
        if len(collected_data) >= 960:
            data_array = np.array(collected_data[-960:]).reshape(1, -1)
            prediction = self.model.predict(data_array)
            movement = np.argmax(prediction)
            self.lblResultado.setText(f"Resultado: {movement}")
            print(f"Movimiento detectado: {movement}")
            send_data(str(movement))
            self.update_indicators(movement)

        if continuarProceso:
            QTimer.singleShot(3000, self.start_collecting_data)

    def update_indicators(self, movement):

        if movement == 0:
            self.frame1.setStyleSheet(estiloAmarillo)
            self.frame2.setStyleSheet(estiloGris)
            self.frame3.setStyleSheet(estiloGris)
            self.frame4.setStyleSheet(estiloGris)
            self.frame5.setStyleSheet(estiloGris)
            self.frame6.setStyleSheet(estiloGris)

        if movement == 1:
            self.frame1.setStyleSheet(estiloGris)
            self.frame2.setStyleSheet(estiloAmarillo)
            self.frame3.setStyleSheet(estiloGris)
            self.frame4.setStyleSheet(estiloGris)
            self.frame5.setStyleSheet(estiloGris)
            self.frame6.setStyleSheet(estiloGris)

        if movement == 2:
            self.frame1.setStyleSheet(estiloGris)
            self.frame2.setStyleSheet(estiloGris)
            self.frame3.setStyleSheet(estiloAmarillo)
            self.frame4.setStyleSheet(estiloGris)
            self.frame5.setStyleSheet(estiloGris)
            self.frame6.setStyleSheet(estiloGris)

        if movement == 3:
            self.frame1.setStyleSheet(estiloGris)
            self.frame2.setStyleSheet(estiloGris)
            self.frame3.setStyleSheet(estiloGris)
            self.frame4.setStyleSheet(estiloAmarillo)
            self.frame5.setStyleSheet(estiloGris)
            self.frame6.setStyleSheet(estiloGris)

        if movement == 4:
            self.frame1.setStyleSheet(estiloGris)
            self.frame2.setStyleSheet(estiloGris)
            self.frame3.setStyleSheet(estiloGris)
            self.frame4.setStyleSheet(estiloGris)
            self.frame5.setStyleSheet(estiloAmarillo)
            self.frame6.setStyleSheet(estiloGris)

        if movement == 5:
            self.frame1.setStyleSheet(estiloGris)
            self.frame2.setStyleSheet(estiloGris)
            self.frame3.setStyleSheet(estiloGris)
            self.frame4.setStyleSheet(estiloGris)
            self.frame5.setStyleSheet(estiloGris)
            self.frame6.setStyleSheet(estiloAmarillo)

        print(movement)

        # Show message only if movement is different from previous and not equal to 1
        if movement != 1 and (
            self.previous_movement is not None and self.previous_movement == movement
        ):
            self.lblResultado.setText("Posición alcanzada")

            pixmap = QPixmap("guide/imagenes/advertencia.png")
            self.imgEstado.setPixmap(pixmap)
            self.imgEstado.setVisible(True)

        else:

            pixmap = QPixmap("guide/imagenes/checked.png")
            self.imgEstado.setPixmap(pixmap)
            self.lblResultado.setText(
                ""
            )  # Clear the message if it's the same or movement is 1

            self.imgEstado.setVisible(False)

        self.previous_movement = movement

    def capturarPuntos(self):

        print("Inicio de captura...")
        self.contadorMuestras = 0
        self.boolCapturaPuntos = True
        self.btncapturar.setVisible(False)

    # INTERFAZ *******************************

    def tonoNotificaciones(self):
        mixer.init()
        mixer.music.load(sonidoNotificacion)
        mixer.music.play()

    def tonoMenu(self):
        mixer.init()
        mixer.music.load(sonidoMouseMove)
        mixer.music.play()

    def tonoClick(self):
        mixer.init()
        mixer.music.load(sonidoMouseClick)
        mixer.music.play()

    def eventFilter(self, object, event):

        if object is self.btnIniciar and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnIniciar.setStyleSheet(estiloBtnHoverAzul2)

            return True

        elif object is self.btnIniciar and event.type() == QtCore.QEvent.Leave:

            self.btnIniciar.setStyleSheet(
                """QWidget { 
                   background-color: #1b1e23;  
                   color: white;
                   font: 12pt "MS Shell Dlg 2";
                    }"""
            )
        return False


class ventanaAdquisicion(QFrame):
    def __init__(self):

        super(ventanaAdquisicion, self).__init__()
        loadUi("guide/ventanas/adquisicion.ui", self)

        self.btnRecolectar.installEventFilter(self)
        self.btnCarpeta.installEventFilter(self)
        self.btnGuardar.installEventFilter(self)
        self.editRuta.setStyleSheet(estiloHoverBlanco)
        self.lblConteo.setStyleSheet(estiloCuenta)

        self.serial_connection = None
        self.reading_thread = None
        self.collecting_data = False
        self.collected_data = []
        self.data_count = 0
        self.start_time = None

        self.filepath = None  # Variable para almacenar la ruta del archivo seleccionado

        self.collect_time_var = 10
        self.repetition_var = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_collect_time)

        self.ON = False
        self.btnRecolectar.clicked.connect(self.start_collecting_data)
        self.btnCarpeta.clicked.connect(self.select_file)
        self.btnGuardar.clicked.connect(self.save_data)

        self.lblAnalizar.setVisible(False)
        pixmap = QPixmap("guide/imagenes/OFF.png")
        self.lblListo.setPixmap(pixmap)

        self.lblConteo.setVisible(False)
        self.lblAnalizar_2.setVisible(False)
        self.pushButton.setVisible(False)
        self.movie = QMovie("guide/imagenes/cerebro2.gif")
        self.lblGif1.setMovie(self.movie)
        self.movie.start()
        self.editRepeticion.setText("1")

    def disconnect_sensor(self):
        if self.reading_thread:
            self.reading_thread.stop()
            self.reading_thread.wait()
            self.update_circle("red")
            print("Conexión cerrada")

    def update_circle(self, color):
        pixmap = QPixmap(50, 50)
        pixmap.fill(QColor(color))
        self.canvas.setPixmap(pixmap)

    def update_data(self, raw_wave_data):
        global collected_data, collecting_data2
        if collecting_data2:
            if self.data_count < 480:
                collected_data.append(raw_wave_data)
                self.data_count += 1
                print("Raw Wave Data:", raw_wave_data)
            if time.time() - self.start_time >= 1:
                self.data_count = 0
                self.start_time = time.time()

    def start_collecting_data(self):
        global collecting_data2, collected_data2, data_count

        self.lblConteo.setVisible(True)
        self.lblAnalizar_2.setVisible(True)
        self.pushButton.setVisible(True)

        self.lblAnalizar.setVisible(True)
        pixmap = QPixmap("guide/imagenes/ON.png")
        self.lblListo.setPixmap(pixmap)

        collecting_data2 = True
        collected_data2 = []
        data_count = 0
        self.start_time = time.time()
        collect_time = int(self.editCuenta.toPlainText())

        data_count = 480 * collect_time

        print(f"Recolección de datos iniciada por {collect_time} segundos.")
        self.timer.start(collect_time * 1000)

        for index in range(collect_time):
            print("conteo: ", index)
            self.lblConteo.setText(str(index + 1) + "/" + self.editCuenta.toPlainText())
            QtTest.QTest.qWait(1000)

    def update_collect_time(self):
        self.stop_collecting_data()
        self.timer.stop()

    def stop_collecting_data(self):
        global collecting_data2, data_count, collected_data2

        self.lblConteo.setVisible(False)
        self.lblAnalizar_2.setVisible(False)
        self.pushButton.setVisible(False)

        collecting_data2 = False

        print(f"Recolección detenida. {len(collected_data2)} datos recolectados.")

        self.lblAnalizar.setVisible(False)
        pixmap = QPixmap("guide/imagenes/OFF.png")
        self.lblListo.setPixmap(pixmap)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Mensaje")
        msg.setText("Proceso de recolección de datos terminado")
        msg.exec_()

    def select_file(self):
        self.filepath, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo", "", "Excel files (*.xlsx);;All files (*)"
        )
        if self.filepath:
            print(f"Archivo seleccionado: {self.filepath}")
            self.editRuta.setText(self.filepath)

    def save_data(self):

        global collected_data2
        if not self.filepath:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Advertencia")
            msg.setText("Seleccione la ubicación del archivo antes de guardar")
            msg.exec_()

            print("Seleccione la ubicación del archivo antes de guardar.")
            return

        try:
            new_data = pd.DataFrame(collected_data2, columns=["Raw Wave Data"])

            if not os.path.exists(self.filepath):
                new_data.to_excel(self.filepath, index=False)
                print(f"Datos guardados en {self.filepath}")

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Mensaje")
                msg.setText("Datos guardados correctamente")
                msg.exec_()

            else:
                existing_data = pd.read_excel(self.filepath)
                new_column_name = f"Raw Wave Data {len(existing_data.columns) + 1}"
                existing_data[new_column_name] = collected_data2
                existing_data.to_excel(self.filepath, index=False)
                print(f"Nueva columna agregada a {self.filepath}")

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Mensaje")
                msg.setText("Nueva columna agregada al archivo")
                msg.exec_()

            current_repetitions = int(self.editRepeticion.toPlainText())
            if current_repetitions > 1:
                self.editRepeticion.setText(str(current_repetitions - 1))
            else:
                self.editRepeticion.setText("1")

        except Exception as e:
            print(f"Error al guardar los datos: {e}")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Algo salio mal al guardar los datos: " + str(e))
            msg.exec_()

    def closeEvent(self, event):
        self.disconnect_sensor()
        event.accept()

    # INTERFAZ *******************************

    def tonoNotificaciones(self):
        mixer.init()
        mixer.music.load(sonidoNotificacion)
        mixer.music.play()

    def tonoMenu(self):
        mixer.init()
        mixer.music.load(sonidoMouseMove)
        mixer.music.play()

    def tonoClick(self):

        mixer.init()
        mixer.music.load(sonidoMouseClick)
        mixer.music.play()

    def eventFilter(self, object, event):

        if object is self.btnRecolectar and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnRecolectar.setStyleSheet(estiloBtnHoverAzul2)

            return True

        elif object is self.btnRecolectar and event.type() == QtCore.QEvent.Leave:

            self.btnRecolectar.setStyleSheet(
                """QWidget { 
                   background-color: #1b1e23;  
                   color: white;
                   font: 12pt "MS Shell Dlg 2";
                    }"""
            )

        if object is self.btnCarpeta and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnCarpeta.setStyleSheet(estiloBtnHoverAzul2)

            return True

        elif object is self.btnCarpeta and event.type() == QtCore.QEvent.Leave:

            self.btnCarpeta.setStyleSheet(
                """QWidget { 
                   background-color: #1b1e23;  
                   color: white;
                   font: 12pt "MS Shell Dlg 2";
                    }"""
            )

        if object is self.btnGuardar and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnGuardar.setStyleSheet(estiloBtnHoverAzul2)

            return True

        elif object is self.btnGuardar and event.type() == QtCore.QEvent.Leave:

            self.btnGuardar.setStyleSheet(
                """QWidget { 
                   background-color: #1b1e23;  
                   color: white;
                   font: 12pt "MS Shell Dlg 2";
                    }"""
            )

        return False


class ventanaGraficas(QFrame):
    def __init__(self):

        super(ventanaGraficas, self).__init__()
        loadUi("guide/ventanas/graficas.ui", self)

        # self.widgetLista = QtWidgets.QListWidget(self.listaDocumentos)

        # Colas para almacenar los datos de la onda cruda
        self.ydata = deque(maxlen=4000)
        self.lock = threading.Lock()

        self.ancho = self.width()
        self.alto = self.height()

        central_widget = QWidget(self)
        central_widget.resize(self.ancho, self.alto - 80)

        layout = QVBoxLayout(central_widget)

        self.btnEscala.installEventFilter(self)
        self.btnIniciar.installEventFilter(self)
        self.editMin.setStyleSheet(estiloHoverEscala)
        self.editMax.setStyleSheet(estiloHoverEscala)

        self.graficarPlot = False

        """
        self.graphWidget = pg.PlotWidget(self.graphicsView)
        self.graphWidget.resize(931, 461)
        self.graphWidget.setBackground("#fff")
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setRange(yRange=[-3000, 3000])

        self.ancho = self.width()
        self.alto = self.height()

        self.graphWidget.setLabel(
            "left",
            "VALOR DE ONDA CRUDA ",
            color="black",
            fontweight="bold",
            fontsize=12,
        )
        self.graphWidget.setLabel(
            "bottom",
            "TIEMPO",
            color="black",
            fontweight="bold",
            fontsize=12,
        )
        """

        # Configurar gráfico
        self.fig, self.ax = plt.subplots(figsize=(10, 5))

        self.fig.set_facecolor("#2c313c")

        # Cambiar el color de las letras de los ejes
        self.ax.set_xlabel("Tiempo", fontsize=12, fontweight="bold", color="white")
        self.ax.set_ylabel(
            "Valor de Onda Cruda", fontsize=12, fontweight="bold", color="white"
        )

        # Cambiar el color de las etiquetas de los ticks
        self.ax.tick_params(axis="x", colors="white")
        self.ax.tick_params(axis="y", colors="white")

        (self.ln,) = plt.plot([], [], "r")
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        self.btnEscala.clicked.connect(self.cambiarEscala)

        self.btnIniciar.clicked.connect(self.graficar)

        # Inicializar la animación como None
        self.ani = None

    def cambiarEscala(self):

        # minimo = int(self.editMin.toPlainText())
        # maximo = int(self.editMax.toPlainText())

        # self.graphWidget.setRange(yRange=[minimo, maximo])
        self.cambio()
        #self.reset_plot()

    def graficar(self):

        print("presionme")

        if self.graficarPlot == False:
            self.graficarPlot = True
            self.btnIniciar.setText("DETENER")

            if self.ani is None:  # Iniciar solo si no está ya en ejecución

                #        self.reset_plot()

                self.ani = FuncAnimation(
                    self.fig,
                    self.update_plot,
                    init_func=self.init_plot,
                    interval=20,
                    blit=True,
                    cache_frame_data=False,
                )

        else:
            self.graficarPlot = False
            self.btnIniciar.setText("INICIAR")
            if self.ani:
                self.ani.event_source.stop()
                self.ani = None

    # self.startCamara()

    # Iniciar el hilo para leer los datos

    #  data_thread = threading.Thread(target=self.read_data)
    #  data_thread.daemon = True
    #  data_thread.start()

    # self.update_plot()

    def read_bytes(self, num_bytes):
        global ser
        data = ser.read(num_bytes)
        if len(data) != num_bytes:
            raise ValueError(
                "No se pudieron leer los bytes suficientes del dispositivo."
            )
        return data

    def parse_packet(self):
        if self.read_bytes(1) != b"\xaa":
            return None
        if self.read_bytes(1) != b"\xaa":
            return None
        payload_length = ord(self.read_bytes(1))
        payload = self.read_bytes(payload_length)
        checksum = ord(self.read_bytes(1))
        if checksum != (255 - sum(payload) & 0xFF):
            print("Checksum incorrecto.")
            return None
        return payload

    def devolverVector(self, vector):
        return vector

    def extract_raw_wave_data(self, payload):
        i = 0
        while i < len(payload):
            code = payload[i]
            i += 1
            if code == 0x80:  # Código de onda cruda (RAW wave data)
                i += 1
                raw_wave_value = struct.unpack(">h", payload[i : i + 2])[0]
                i += 2
                return raw_wave_value
        return None

    def apagar(self):
        global collecting_data
        collecting_data = False

    def read_data(self):
        global ser, dataY, collected_data, collected_data2, data_count, collecting_data, collecting_data2

        while ser and ser.is_open:
            packet = self.parse_packet()
            if packet:
                raw_wave_data = self.extract_raw_wave_data(packet)
                if raw_wave_data is not None:
                    with self.lock:
                        self.ydata.append(raw_wave_data)
                        dataY.append(raw_wave_data)
                        if collecting_data:
                            collected_data.append(raw_wave_data)
                            print("Raw Wave Data:", raw_wave_data)

                        if collecting_data2 and len(collected_data2) < data_count:
                            collected_data2.append(raw_wave_data)
                            print("Raw Wave Data:", raw_wave_data)

                    # print(self.ydata)

    def cambio(self):
        minimo = int(self.editMin.toPlainText())
        maximo = int(self.editMax.toPlainText())
        self.ax.set_ylim(minimo, maximo)

    def reset_plot(self):
        # Limpiar el contenido actual del gráfico
        self.ax.cla()
        # Inicializar de nuevo el gráfico
        self.init_plot()
        # Redibujar el canvas
        self.canvas.draw()

    def init_plot(self):
        minimo = int(self.editMin.toPlainText())
        maximo = int(self.editMax.toPlainText())

        self.ax.set_xlim(0, 2000)
        self.ax.set_ylim(minimo, maximo)
        return (self.ln,)

    def update_plot(self, frame):
        global dataY
        with self.lock:
            if len(dataY) > 0:
                # self.ax.relim()
                # Cambiar el color de las letras de los ejes
                self.ax.set_xlabel(
                    "Tiempo", fontsize=12, fontweight="bold", color="white"
                )
                self.ax.set_ylabel(
                    "Valor de Onda Cruda", fontsize=12, fontweight="bold", color="white"
                )

                self.ln.set_data(range(len(dataY)), dataY)
                self.ax.set_xlim(max(0, len(dataY) - 2000), len(dataY))
                self.canvas.draw()
        return (self.ln,)

    def eventFilter(self, object, event):

        if object is self.btnIniciar and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnIniciar.setStyleSheet(estiloBtnHoverAzul2)
            return True

        elif object is self.btnIniciar and event.type() == QtCore.QEvent.Leave:

            self.btnIniciar.setStyleSheet(
                """QWidget { 
                   background-color: #1b1e23;  
                   color: white;
                   font: 12pt "MS Shell Dlg 2";
                    }"""
            )

        if object is self.btnEscala and event.type() == QtCore.QEvent.Enter:

            self.tonoMenu()
            self.btnEscala.setStyleSheet(estiloBtnCamaraON)

            return True

        elif object is self.btnEscala and event.type() == QtCore.QEvent.Leave:

            self.btnEscala.setStyleSheet(estiloBtnNormal2)

        return False

    def tonoMenu(self):
        mixer.init()
        mixer.music.load(sonidoMouseMove)
        mixer.music.play()

    def tonoClick(self):

        mixer.init()
        mixer.music.load(sonidoMouseClick)
        mixer.music.play()


class itemsRegistros(QFrame):
    def __init__(self):
        super(itemsRegistros, self).__init__()
        loadUi("guide/ventanas/itemsLista.ui", self)

    def parametrosLista(self, icono, nombre, fecha, descripcion):
        self.lblIcono.setPixmap(QPixmap(icono))
        self.lblNombre.setText(nombre)
        self.lblFecha.setText(fecha)
        self.lblDescripcion.setText(descripcion)

        self.lblNombre.setStyleSheet(estiloTextoLista)
        self.lblDescripcion.setStyleSheet(estiloTextoLista)
        self.lblFecha.setStyleSheet(estiloTextoFecha)

    def getNombre(self):
        return self.lblNombre.text()


class Notificaciones(QFrame):
    def __init__(self):
        super(Notificaciones, self).__init__()
        loadUi("guide/ventanas/notificaciones.ui", self)
        self.setStyleSheet(estiloFondoNotificacion)

    def parametrosNotificacion(self, icono, titulo, descripcion):
        self.lblIcono.setPixmap(QPixmap(icono))
        self.lblNombre.setText(titulo)
        self.lbldescripcion.setText(descripcion)

        self.lblNombre.setStyleSheet(estiloNotificacionNombre)
        self.lbldescripcion.setStyleSheet(estiloNotificacionDescripcion)
        # self.lblFecha.setStyleSheet(estiloTextoFecha)


class ventanaAcerca(QFrame):
    def __init__(self):
        super(ventanaAcerca, self).__init__()
        loadUi("guide/ventanas/acerca.ui", self)


if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = ventanaPrincipal()
    window.show()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())
