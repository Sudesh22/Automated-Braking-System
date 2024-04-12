import os
import sys, time
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtSvg, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStackedWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QScrollArea, QGridLayout, QGroupBox, QRadioButton, QFrame, QCalendarWidget, QMessageBox, QProgressBar
from PyQt5.QtCore import *
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
# os.system("pyuic5 -o interface_ui.py interface.ui")
# os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui.oQCkCR")

################################################################################################
# Import the generated UI
################################################################################################
from interface_ui import *
################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        for i in range(120):
            self.ui.widget.updateValue(i+1)
            time.sleep(0.1)
            QApplication.processEvents()
    
        ################################################################################################
        # Show window
        ################################################################################################

########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  