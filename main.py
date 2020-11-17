import sys
from PyQt5 import QtWidgets
import qdarkstyle
from PyQt5.QtCore import QThreadPool, QSettings, QCoreApplication
from pyqtgraph.Qt import QtGui
import ctypes

from ui_files.ui_mainwindow import Ui_MainWindow
import os

myappid = 'nasstrom.giwaxs.0.0.1'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

ORGANIZATION_NAME = 'nasstrom-inc'
ORGANIZATION_DOMAIN = 'https://github.com/hampusnasstrom'
APPLICATION_NAME = 'giwaxs_broadening'

os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt5'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.thread_pool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.thread_pool.maxThreadCount())

        self.setupUi(self)


if __name__ == '__main__':
    QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QtGui.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api=os.environ['PYQTGRAPH_QT_LIB']))
    window = MainWindow()
    window.show()
    app.exec_()