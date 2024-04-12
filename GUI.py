import sys, os, serial, time
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar
from PyQt5.QtCore import *
from PyQt5.QtGui import QCursor
from interface_ui import *

if getattr(sys, 'frozen', False):
        curr_path = os.path.dirname(sys.executable)
elif __file__:
        curr_path = os.path.dirname(__file__)
print(curr_path)


try:
    ser = serial.Serial("COM3", 9600)

    class ProgressBar_(QProgressBar):
        def __init__(self, parent=None):
            super().__init__(parent)
            self._active = False
            self.setOrientation(QtCore.Qt.Vertical)
            self.setFormat("%p")
            self.setGeometry(0,0,27,260)
            self.setStyleSheet("""QProgressBar {background-color: rgb(98, 114, 164);color: rgb(200, 200, 200);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 10px;background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop: 1 rgba(170, 85, 255, 255));} QProgressBar:focus{outline: 0;border:none;}""")

        def updateVal(self, val):
            val = int(val)
            if val <= 25:
                self.setStyleSheet("""QProgressBar {background-color: rgb(98, 114, 164);color: rgb(200, 200, 200);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 10px;background-color:qlineargradient(spread:pad, x1:1, y1:0.489, x2:0, y2:0.465591, stop:0.242718 rgba(111, 214, 90, 255), stop:0.995283 rgba(74, 244, 0, 255));} QProgressBar:focus{outline: 0;border:none;}""")
            if ((val <= 75)and(val > 25)):
                self.setStyleSheet("""QProgressBar {background-color: rgb(98, 114, 164);color: rgb(200, 200, 200);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 10px;background-color:qlineargradient(spread:pad, x1:1, y1:0.489, x2:0, y2:0.465591, stop:0.242718 rgba(194, 214, 90, 255), stop:0.995283 rgba(244, 181, 0, 255));} QProgressBar:focus{outline: 0;border:none;}""")
            if ((val <= 100)and(val > 75)):
                self.setStyleSheet("""QProgressBar {background-color: rgb(98, 114, 164);color: rgb(200, 200, 200);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 10px;background-color:qlineargradient(spread:pad, x1:1, y1:0.489, x2:0, y2:0.465591, stop:0.242718 rgba(214, 90, 91, 255), stop:0.995283 rgba(244, 0, 0, 255));} QProgressBar:focus{outline: 0;border:none;}""")
            self.setMaximum(100)
            self.setValue(val)
            QApplication.processEvents()
    

    class Display(QMainWindow):
        def __init__(self):
            super(Display, self).__init__()
            loadUi(os.path.join(curr_path,'.ui\Dashboard.ui'), self)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.label1 = ProgressBar_()

            scene1 = QtWidgets.QGraphicsScene(self.graphicsView_1)
            self.graphicsView_1.setScene(scene1)
            proxy1 = QtWidgets.QGraphicsProxyWidget()
            self.graphicsView_1.setStyleSheet("""QGraphicsView{background-color: rgb(98, 114, 164);}""")

            proxy1.setWidget(self.label1)

            scene1.addItem(proxy1)
            self.timer = QTimer()
            self.timer.timeout.connect(self.update)
            self.timer.start(35)
            
            self.Meter.setMouseTracking(False)
            self.Meter.setScaleValueColor(225,225,0)
            

        def update(self):
            count = 0
            first = 0

            while 1:
                val_ue = ser.readline().decode()
                speed,safe_d,distance,exp, flag = val_ue.split(",")
                print(speed,"-",safe_d,"-",distance,"-",exp,"-", flag)
                global v
                if first:
                    pass
                else:
                    v = int(speed)
                    first = 1
                if int(flag):
                    v = int(speed)
                    v -= count
                    self.Status.setText("Alert!")
                    self.Status.setStyleSheet("""background-color: rgb(255, 14, 14);border-radius: 20px;text-align: center;""")
                    self.label1.updateVal(int(int(exp)/2.55))
                    self.Meter.updateValue(int(v))
                    QApplication.processEvents()
                    count+=1
                else:
                    self.Meter.updateValue(int(v))
                    self.label1.updateVal(int(0))
                    self.Status.setText("Safe")
                    self.Status.setStyleSheet("""background-color: rgb(0, 255, 29);border-radius: 20px;text-align: center;""")
                    if v<int(speed):
                        count -= 1
                        v += 1

                QApplication.processEvents()
                time.sleep(0.1)
                    
        def mousePressEvent(self, event):
            if event.button()==Qt.LeftButton:
                self.m_flag=True
                self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
                event.accept()
                self.setCursor(QCursor(Qt.OpenHandCursor)) #Change the mouse icon
                
        def mouseMoveEvent(self, QMouseEvent):
            if Qt.LeftButton and self.m_flag:  
                self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
                QMouseEvent.accept()
                
        def mouseReleaseEvent(self, QMouseEvent):
            self.m_flag=False
            self.setCursor(QCursor(Qt.ArrowCursor))

    def main():
        global app
        app = QApplication(sys.argv)
        disp = Display()
        disp.show()
        sys.exit(app.exec_())

    if __name__ == '__main__':
        main()

except serial.serialutil.SerialException:
    print("Arduino not connected....")