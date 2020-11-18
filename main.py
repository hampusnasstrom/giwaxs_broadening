import sys
from PyQt5 import QtWidgets
import qdarkstyle
from PyQt5.QtCore import QThreadPool, QSettings, QCoreApplication, pyqtSlot
from pyqtgraph.Qt import QtGui
import ctypes

from ProjectionModel import ProjectionModel
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

        self.model = ProjectionModel()

    @pyqtSlot(int)
    def set_diameter(self, diameter: int):
        self.model.set_beam_diameter(diameter)
        print('Broadening is %.5f deg. 2theta' % self.model.get_broadening())

    @pyqtSlot(int)
    def set_divergence(self, divergence: int):
        self.model.set_radial_divergence(divergence)
        print('Broadening is %.5f deg. 2theta' % self.model.get_broadening())

    @pyqtSlot(int)
    def set_incidence(self, incidence: int):
        self.model.set_chi(incidence)
        print('Broadening is %.5f deg. 2theta' % self.model.get_broadening())

    @pyqtSlot(int)
    def set_x_pos(self, x_pos: int):
        self.model.set_x_det(x_pos)
        print('Broadening is %.5f deg. 2theta' % self.model.get_broadening())

    @pyqtSlot(int)
    def set_y_pos(self, y_pos: int):
        pass

    @pyqtSlot(int)
    def set_z_pos(self, z_pos: int):
        pass


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