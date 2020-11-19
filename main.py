import sys
from PyQt5 import QtWidgets
import qdarkstyle
from PyQt5.QtCore import QThreadPool, QSettings, QCoreApplication, pyqtSlot
from pyqtgraph.Qt import QtGui
import ctypes

import pyqtgraph as pg

from GiwaxsDetector import Detector
from ProjectionModel import ProjectionModel
from ui_files.ui_mainwindow import Ui_MainWindow
import os
import numpy as np

myappid = 'nasstrom.giwaxs.0.0.1'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

ORGANIZATION_NAME = 'nasstrom-inc'
ORGANIZATION_DOMAIN = 'https://github.com/hampusnasstrom'
APPLICATION_NAME = 'giwaxs_broadening'

os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt5'
pg.setConfigOption('background', pg.mkColor(25, 35, 45))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.thread_pool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.thread_pool.maxThreadCount())

        self.setupUi(self)

        self.plot_item = self.graphics_layout.addPlot()
        self._plot_ref = None

        self.model = ProjectionModel()
        self.detector = Detector(detector='pilatus_1m')

        self.eval_points = 1043
        self.two_theta = np.zeros(self.eval_points)

    def update_plot(self):
        # Check if first time plotting
        if not self._plot_ref:
            # If first time, add plot
            self._plot_ref = self.plot_item.plot(self.two_theta, self.model.get_broadening().reshape((-1,)))
        else:
            # Else, update previous plot
            self._plot_ref.setData(self.two_theta, self.model.get_broadening().reshape((-1,)))

    @pyqtSlot(int)
    def set_diameter(self, diameter: int):
        self.model.set_beam_diameter(diameter)
        self.update_plot()

    @pyqtSlot(int)
    def set_divergence(self, divergence: int):
        self.model.set_radial_divergence(divergence)
        self.update_plot()

    @pyqtSlot(int)
    def set_incidence(self, incidence: int):
        self.model.set_chi(incidence)
        self.update_plot()

    @pyqtSlot(int)
    def set_x_pos(self, x_pos: int):
        self.model.set_x_det(x_pos)
        self.detector.set_x_pos(x_pos)
        two_theta_low, two_theta_high = self.detector.get_two_theta()
        self.two_theta = np.linspace(two_theta_low, two_theta_high, self.eval_points)
        self.model.set_two_theta(self.two_theta)
        self.update_plot()
        # print('Broadening is %.5f deg. 2theta' % self.model.get_broadening())

    @pyqtSlot(int)
    def set_y_pos(self, y_pos: int):
        pass

    @pyqtSlot(int)
    def set_z_pos(self, z_pos: int):
        self.detector.set_z_pos(z_pos)
        two_theta_low, two_theta_high = self.detector.get_two_theta()
        self.two_theta = np.linspace(two_theta_low, two_theta_high, self.eval_points)
        self.model.set_two_theta(self.two_theta)
        self.update_plot()


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