# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 945)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gb_beam = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_beam.sizePolicy().hasHeightForWidth())
        self.gb_beam.setSizePolicy(sizePolicy)
        self.gb_beam.setObjectName("gb_beam")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gb_beam)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.divergence = QtWidgets.QWidget(self.gb_beam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.divergence.sizePolicy().hasHeightForWidth())
        self.divergence.setSizePolicy(sizePolicy)
        self.divergence.setObjectName("divergence")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.divergence)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.sb_divergence = QtWidgets.QDoubleSpinBox(self.divergence)
        self.sb_divergence.setObjectName("sb_divergence")
        self.gridLayout_6.addWidget(self.sb_divergence, 1, 0, 1, 2)
        self.label_middle_divergence = QtWidgets.QLabel(self.divergence)
        self.label_middle_divergence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_divergence.setObjectName("label_middle_divergence")
        self.gridLayout_6.addWidget(self.label_middle_divergence, 3, 0, 1, 1)
        self.label_top_divergence = QtWidgets.QLabel(self.divergence)
        self.label_top_divergence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_divergence.setObjectName("label_top_divergence")
        self.gridLayout_6.addWidget(self.label_top_divergence, 2, 0, 1, 1)
        self.label_bottom_divergence = QtWidgets.QLabel(self.divergence)
        self.label_bottom_divergence.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_divergence.setObjectName("label_bottom_divergence")
        self.gridLayout_6.addWidget(self.label_bottom_divergence, 4, 0, 1, 1)
        self.slider_divergence = QtWidgets.QSlider(self.divergence)
        self.slider_divergence.setMaximum(30)
        self.slider_divergence.setPageStep(5)
        self.slider_divergence.setOrientation(QtCore.Qt.Vertical)
        self.slider_divergence.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_divergence.setTickInterval(5)
        self.slider_divergence.setObjectName("slider_divergence")
        self.gridLayout_6.addWidget(self.slider_divergence, 2, 1, 3, 1)
        self.label_divergence = QtWidgets.QLabel(self.divergence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_divergence.sizePolicy().hasHeightForWidth())
        self.label_divergence.setSizePolicy(sizePolicy)
        self.label_divergence.setObjectName("label_divergence")
        self.gridLayout_6.addWidget(self.label_divergence, 0, 0, 1, 2)
        self.gridLayout_8.addWidget(self.divergence, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gb_beam)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_8.addWidget(self.line_4, 0, 1, 1, 1)
        self.diameter = QtWidgets.QWidget(self.gb_beam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter.sizePolicy().hasHeightForWidth())
        self.diameter.setSizePolicy(sizePolicy)
        self.diameter.setObjectName("diameter")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.diameter)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_diameter = QtWidgets.QLabel(self.diameter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_diameter.sizePolicy().hasHeightForWidth())
        self.label_diameter.setSizePolicy(sizePolicy)
        self.label_diameter.setObjectName("label_diameter")
        self.gridLayout_7.addWidget(self.label_diameter, 0, 0, 1, 2)
        self.slider_diameter = QtWidgets.QSlider(self.diameter)
        self.slider_diameter.setMaximum(5000)
        self.slider_diameter.setSingleStep(50)
        self.slider_diameter.setPageStep(500)
        self.slider_diameter.setProperty("value", 100)
        self.slider_diameter.setOrientation(QtCore.Qt.Vertical)
        self.slider_diameter.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_diameter.setTickInterval(5)
        self.slider_diameter.setObjectName("slider_diameter")
        self.gridLayout_7.addWidget(self.slider_diameter, 2, 1, 3, 1)
        self.sb_diameter = QtWidgets.QSpinBox(self.diameter)
        self.sb_diameter.setMaximum(5000)
        self.sb_diameter.setProperty("value", 100)
        self.sb_diameter.setObjectName("sb_diameter")
        self.gridLayout_7.addWidget(self.sb_diameter, 1, 0, 1, 2)
        self.label_bottom_diameter = QtWidgets.QLabel(self.diameter)
        self.label_bottom_diameter.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_diameter.setObjectName("label_bottom_diameter")
        self.gridLayout_7.addWidget(self.label_bottom_diameter, 4, 0, 1, 1)
        self.label_top_diameter = QtWidgets.QLabel(self.diameter)
        self.label_top_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_diameter.setObjectName("label_top_diameter")
        self.gridLayout_7.addWidget(self.label_top_diameter, 2, 0, 1, 1)
        self.label_middle_diameter = QtWidgets.QLabel(self.diameter)
        self.label_middle_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_diameter.setObjectName("label_middle_diameter")
        self.gridLayout_7.addWidget(self.label_middle_diameter, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.diameter, 0, 2, 1, 1)
        self.frame_beam = QtWidgets.QFrame(self.gb_beam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_beam.sizePolicy().hasHeightForWidth())
        self.frame_beam.setSizePolicy(sizePolicy)
        self.frame_beam.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_beam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_beam.setObjectName("frame_beam")
        self.formLayout = QtWidgets.QFormLayout(self.frame_beam)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_beam)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sb_energy = QtWidgets.QDoubleSpinBox(self.frame_beam)
        self.sb_energy.setObjectName("sb_energy")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sb_energy)
        self.label_3 = QtWidgets.QLabel(self.frame_beam)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.sb_wavelength = QtWidgets.QDoubleSpinBox(self.frame_beam)
        self.sb_wavelength.setObjectName("sb_wavelength")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sb_wavelength)
        self.label_4 = QtWidgets.QLabel(self.frame_beam)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cb_source = QtWidgets.QComboBox(self.frame_beam)
        self.cb_source.setObjectName("cb_source")
        self.cb_source.addItem("")
        self.cb_source.addItem("")
        self.cb_source.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_source)
        self.gridLayout_8.addWidget(self.frame_beam, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.gb_beam)
        self.gb_incidence = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_incidence.sizePolicy().hasHeightForWidth())
        self.gb_incidence.setSizePolicy(sizePolicy)
        self.gb_incidence.setObjectName("gb_incidence")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gb_incidence)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.incidence = QtWidgets.QWidget(self.gb_incidence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.incidence.sizePolicy().hasHeightForWidth())
        self.incidence.setSizePolicy(sizePolicy)
        self.incidence.setObjectName("incidence")
        self.gridLayout = QtWidgets.QGridLayout(self.incidence)
        self.gridLayout.setObjectName("gridLayout")
        self.label_incidence = QtWidgets.QLabel(self.incidence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_incidence.sizePolicy().hasHeightForWidth())
        self.label_incidence.setSizePolicy(sizePolicy)
        self.label_incidence.setObjectName("label_incidence")
        self.gridLayout.addWidget(self.label_incidence, 0, 0, 1, 2)
        self.sb_incidence = QtWidgets.QDoubleSpinBox(self.incidence)
        self.sb_incidence.setProperty("value", 2.0)
        self.sb_incidence.setObjectName("sb_incidence")
        self.gridLayout.addWidget(self.sb_incidence, 1, 0, 1, 2)
        self.label_top_incidence = QtWidgets.QLabel(self.incidence)
        self.label_top_incidence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_incidence.setObjectName("label_top_incidence")
        self.gridLayout.addWidget(self.label_top_incidence, 2, 0, 1, 1)
        self.slider_incidence = QtWidgets.QSlider(self.incidence)
        self.slider_incidence.setMaximum(30)
        self.slider_incidence.setPageStep(5)
        self.slider_incidence.setProperty("value", 2)
        self.slider_incidence.setOrientation(QtCore.Qt.Vertical)
        self.slider_incidence.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_incidence.setTickInterval(5)
        self.slider_incidence.setObjectName("slider_incidence")
        self.gridLayout.addWidget(self.slider_incidence, 2, 1, 3, 1)
        self.label_middle_incidence = QtWidgets.QLabel(self.incidence)
        self.label_middle_incidence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_incidence.setObjectName("label_middle_incidence")
        self.gridLayout.addWidget(self.label_middle_incidence, 3, 0, 1, 1)
        self.label_bottom_incidence = QtWidgets.QLabel(self.incidence)
        self.label_bottom_incidence.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_incidence.setObjectName("label_bottom_incidence")
        self.gridLayout.addWidget(self.label_bottom_incidence, 4, 0, 1, 1)
        self.gridLayout_9.addWidget(self.incidence, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gb_incidence)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_9.addWidget(self.line, 0, 1, 1, 1)
        self.diffraction = QtWidgets.QWidget(self.gb_incidence)
        self.diffraction.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diffraction.sizePolicy().hasHeightForWidth())
        self.diffraction.setSizePolicy(sizePolicy)
        self.diffraction.setObjectName("diffraction")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.diffraction)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_diffraction = QtWidgets.QLabel(self.diffraction)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_diffraction.sizePolicy().hasHeightForWidth())
        self.label_diffraction.setSizePolicy(sizePolicy)
        self.label_diffraction.setObjectName("label_diffraction")
        self.gridLayout_5.addWidget(self.label_diffraction, 0, 0, 1, 2)
        self.sb_incidence_diffraction = QtWidgets.QDoubleSpinBox(self.diffraction)
        self.sb_incidence_diffraction.setObjectName("sb_incidence_diffraction")
        self.gridLayout_5.addWidget(self.sb_incidence_diffraction, 1, 0, 1, 2)
        self.label_top_diffraction = QtWidgets.QLabel(self.diffraction)
        self.label_top_diffraction.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_diffraction.setObjectName("label_top_diffraction")
        self.gridLayout_5.addWidget(self.label_top_diffraction, 2, 0, 1, 1)
        self.slider_diffraction = QtWidgets.QSlider(self.diffraction)
        self.slider_diffraction.setOrientation(QtCore.Qt.Vertical)
        self.slider_diffraction.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_diffraction.setTickInterval(5)
        self.slider_diffraction.setObjectName("slider_diffraction")
        self.gridLayout_5.addWidget(self.slider_diffraction, 2, 1, 3, 1)
        self.label_middle_diffraction = QtWidgets.QLabel(self.diffraction)
        self.label_middle_diffraction.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_diffraction.setObjectName("label_middle_diffraction")
        self.gridLayout_5.addWidget(self.label_middle_diffraction, 3, 0, 1, 1)
        self.label_bottom_diffraction = QtWidgets.QLabel(self.diffraction)
        self.label_bottom_diffraction.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_diffraction.setObjectName("label_bottom_diffraction")
        self.gridLayout_5.addWidget(self.label_bottom_diffraction, 4, 0, 1, 1)
        self.gridLayout_9.addWidget(self.diffraction, 0, 2, 1, 1)
        self.frame_sample = QtWidgets.QFrame(self.gb_incidence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_sample.sizePolicy().hasHeightForWidth())
        self.frame_sample.setSizePolicy(sizePolicy)
        self.frame_sample.setMinimumSize(QtCore.QSize(0, 92))
        self.frame_sample.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sample.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sample.setObjectName("frame_sample")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_sample)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_sample)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cb_material = QtWidgets.QComboBox(self.frame_sample)
        self.cb_material.setObjectName("cb_material")
        self.cb_material.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_material)
        self.gridLayout_9.addWidget(self.frame_sample, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.gb_incidence)
        self.gb_x_det = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_x_det.sizePolicy().hasHeightForWidth())
        self.gb_x_det.setSizePolicy(sizePolicy)
        self.gb_x_det.setObjectName("gb_x_det")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gb_x_det)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.y_det = QtWidgets.QWidget(self.gb_x_det)
        self.y_det.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_det.sizePolicy().hasHeightForWidth())
        self.y_det.setSizePolicy(sizePolicy)
        self.y_det.setObjectName("y_det")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.y_det)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.slider_incidence_y_det = QtWidgets.QSlider(self.y_det)
        self.slider_incidence_y_det.setMaximum(2000)
        self.slider_incidence_y_det.setOrientation(QtCore.Qt.Vertical)
        self.slider_incidence_y_det.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_incidence_y_det.setTickInterval(5)
        self.slider_incidence_y_det.setObjectName("slider_incidence_y_det")
        self.gridLayout_3.addWidget(self.slider_incidence_y_det, 2, 1, 3, 1)
        self.label_y_det = QtWidgets.QLabel(self.y_det)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_y_det.sizePolicy().hasHeightForWidth())
        self.label_y_det.setSizePolicy(sizePolicy)
        self.label_y_det.setObjectName("label_y_det")
        self.gridLayout_3.addWidget(self.label_y_det, 0, 0, 1, 2)
        self.label_middle_y_det = QtWidgets.QLabel(self.y_det)
        self.label_middle_y_det.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_y_det.setObjectName("label_middle_y_det")
        self.gridLayout_3.addWidget(self.label_middle_y_det, 3, 0, 1, 1)
        self.sb_incidence_y_det = QtWidgets.QDoubleSpinBox(self.y_det)
        self.sb_incidence_y_det.setObjectName("sb_incidence_y_det")
        self.gridLayout_3.addWidget(self.sb_incidence_y_det, 1, 0, 1, 2)
        self.label_top_y_det = QtWidgets.QLabel(self.y_det)
        self.label_top_y_det.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_y_det.setObjectName("label_top_y_det")
        self.gridLayout_3.addWidget(self.label_top_y_det, 2, 0, 1, 1)
        self.label_bottom_y_det = QtWidgets.QLabel(self.y_det)
        self.label_bottom_y_det.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_y_det.setObjectName("label_bottom_y_det")
        self.gridLayout_3.addWidget(self.label_bottom_y_det, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.y_det, 0, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gb_x_det)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_10.addWidget(self.line_3, 0, 3, 1, 1)
        self.x_det = QtWidgets.QWidget(self.gb_x_det)
        self.x_det.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.x_det.sizePolicy().hasHeightForWidth())
        self.x_det.setSizePolicy(sizePolicy)
        self.x_det.setObjectName("x_det")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.x_det)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.slider_incidence_x_det = QtWidgets.QSlider(self.x_det)
        self.slider_incidence_x_det.setMaximum(2000)
        self.slider_incidence_x_det.setProperty("value", 300)
        self.slider_incidence_x_det.setOrientation(QtCore.Qt.Vertical)
        self.slider_incidence_x_det.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_incidence_x_det.setTickInterval(5)
        self.slider_incidence_x_det.setObjectName("slider_incidence_x_det")
        self.gridLayout_2.addWidget(self.slider_incidence_x_det, 2, 1, 3, 1)
        self.label = QtWidgets.QLabel(self.x_det)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.label_middle_x_det = QtWidgets.QLabel(self.x_det)
        self.label_middle_x_det.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_x_det.setObjectName("label_middle_x_det")
        self.gridLayout_2.addWidget(self.label_middle_x_det, 3, 0, 1, 1)
        self.sb_incidence_x_det = QtWidgets.QDoubleSpinBox(self.x_det)
        self.sb_incidence_x_det.setMaximum(2000.0)
        self.sb_incidence_x_det.setProperty("value", 300.0)
        self.sb_incidence_x_det.setObjectName("sb_incidence_x_det")
        self.gridLayout_2.addWidget(self.sb_incidence_x_det, 1, 0, 1, 2)
        self.label_top_x_det = QtWidgets.QLabel(self.x_det)
        self.label_top_x_det.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_x_det.setObjectName("label_top_x_det")
        self.gridLayout_2.addWidget(self.label_top_x_det, 2, 0, 1, 1)
        self.label_bottom_x_det = QtWidgets.QLabel(self.x_det)
        self.label_bottom_x_det.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_x_det.setObjectName("label_bottom_x_det")
        self.gridLayout_2.addWidget(self.label_bottom_x_det, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.x_det, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gb_x_det)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_10.addWidget(self.line_2, 0, 1, 1, 1)
        self.z_det = QtWidgets.QWidget(self.gb_x_det)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_det.sizePolicy().hasHeightForWidth())
        self.z_det.setSizePolicy(sizePolicy)
        self.z_det.setObjectName("z_det")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.z_det)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.slider_incidence_z_det = QtWidgets.QSlider(self.z_det)
        self.slider_incidence_z_det.setMaximum(2000)
        self.slider_incidence_z_det.setOrientation(QtCore.Qt.Vertical)
        self.slider_incidence_z_det.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_incidence_z_det.setTickInterval(5)
        self.slider_incidence_z_det.setObjectName("slider_incidence_z_det")
        self.gridLayout_4.addWidget(self.slider_incidence_z_det, 2, 1, 3, 1)
        self.label_z_det = QtWidgets.QLabel(self.z_det)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_z_det.sizePolicy().hasHeightForWidth())
        self.label_z_det.setSizePolicy(sizePolicy)
        self.label_z_det.setObjectName("label_z_det")
        self.gridLayout_4.addWidget(self.label_z_det, 0, 0, 1, 2)
        self.label_middle_z_det = QtWidgets.QLabel(self.z_det)
        self.label_middle_z_det.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_middle_z_det.setObjectName("label_middle_z_det")
        self.gridLayout_4.addWidget(self.label_middle_z_det, 3, 0, 1, 1)
        self.sb_incidence_z_det = QtWidgets.QDoubleSpinBox(self.z_det)
        self.sb_incidence_z_det.setObjectName("sb_incidence_z_det")
        self.gridLayout_4.addWidget(self.sb_incidence_z_det, 1, 0, 1, 2)
        self.label_top_z_det = QtWidgets.QLabel(self.z_det)
        self.label_top_z_det.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_top_z_det.setObjectName("label_top_z_det")
        self.gridLayout_4.addWidget(self.label_top_z_det, 2, 0, 1, 1)
        self.label_bottom_z_det = QtWidgets.QLabel(self.z_det)
        self.label_bottom_z_det.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_bottom_z_det.setObjectName("label_bottom_z_det")
        self.gridLayout_4.addWidget(self.label_bottom_z_det, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.z_det, 0, 4, 1, 1)
        self.frame_detector = QtWidgets.QFrame(self.gb_x_det)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_detector.sizePolicy().hasHeightForWidth())
        self.frame_detector.setSizePolicy(sizePolicy)
        self.frame_detector.setMinimumSize(QtCore.QSize(0, 92))
        self.frame_detector.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_detector.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_detector.setObjectName("frame_detector")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_detector)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_detector)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.frame_detector)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout_10.addWidget(self.frame_detector, 1, 0, 1, 5)
        self.horizontalLayout.addWidget(self.gb_x_det)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphics_layout = GraphicsLayoutWidget(self.dockWidgetContents)
        self.graphics_layout.setMinimumSize(QtCore.QSize(600, 500))
        self.graphics_layout.setObjectName("graphics_layout")
        self.verticalLayout.addWidget(self.graphics_layout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.slider_incidence.valueChanged['int'].connect(MainWindow.set_incidence)
        self.slider_divergence.valueChanged['int'].connect(MainWindow.set_divergence)
        self.slider_diameter.valueChanged['int'].connect(MainWindow.set_diameter)
        self.slider_incidence_x_det.valueChanged['int'].connect(MainWindow.set_x_pos)
        self.slider_incidence_y_det.valueChanged['int'].connect(MainWindow.set_y_pos)
        self.slider_incidence_z_det.valueChanged['int'].connect(MainWindow.set_z_pos)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gb_beam.setTitle(_translate("MainWindow", "Beam"))
        self.label_middle_divergence.setText(_translate("MainWindow", "15"))
        self.label_top_divergence.setText(_translate("MainWindow", "30"))
        self.label_bottom_divergence.setText(_translate("MainWindow", "0"))
        self.label_divergence.setText(_translate("MainWindow", "<html><head/><body><p>Divergence<br/>radial [mrad]</p></body></html>"))
        self.label_diameter.setText(_translate("MainWindow", "<html><head/><body><p>Diameter<br/>[μm]</p></body></html>"))
        self.label_bottom_diameter.setText(_translate("MainWindow", "0"))
        self.label_top_diameter.setText(_translate("MainWindow", "5000"))
        self.label_middle_diameter.setText(_translate("MainWindow", "2500"))
        self.label_2.setText(_translate("MainWindow", "Energy [keV]:"))
        self.label_3.setText(_translate("MainWindow", "Wavelength [Å]:"))
        self.label_4.setText(_translate("MainWindow", "Source:"))
        self.cb_source.setItemText(0, _translate("MainWindow", "Ga"))
        self.cb_source.setItemText(1, _translate("MainWindow", "Cu"))
        self.cb_source.setItemText(2, _translate("MainWindow", "Custom"))
        self.gb_incidence.setTitle(_translate("MainWindow", "Sample"))
        self.label_incidence.setText(_translate("MainWindow", "<html><head/><body><p>Incidence<br/>angle [<span style=\" font-weight:600;\">°</span>]</p></body></html>"))
        self.label_top_incidence.setText(_translate("MainWindow", "30"))
        self.label_middle_incidence.setText(_translate("MainWindow", "15"))
        self.label_bottom_incidence.setText(_translate("MainWindow", "0"))
        self.label_diffraction.setText(_translate("MainWindow", "<html><head/><body><p>Diffraction<br/>angle [<span style=\" font-weight:600;\">°</span>]</p></body></html>"))
        self.label_top_diffraction.setText(_translate("MainWindow", "80"))
        self.label_middle_diffraction.setText(_translate("MainWindow", "40"))
        self.label_bottom_diffraction.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Material:"))
        self.cb_material.setItemText(0, _translate("MainWindow", "LaB6"))
        self.gb_x_det.setTitle(_translate("MainWindow", "Detector"))
        self.label_y_det.setText(_translate("MainWindow", "<html><head/><body><p>Position<br/>-y [mm]</p></body></html>"))
        self.label_middle_y_det.setText(_translate("MainWindow", "1000"))
        self.label_top_y_det.setText(_translate("MainWindow", "2000"))
        self.label_bottom_y_det.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Position<br/>-x [mm]</p></body></html>"))
        self.label_middle_x_det.setText(_translate("MainWindow", "1000"))
        self.label_top_x_det.setText(_translate("MainWindow", "2000"))
        self.label_bottom_x_det.setText(_translate("MainWindow", "0"))
        self.label_z_det.setText(_translate("MainWindow", "<html><head/><body><p>Position<br/>-z [mm]</p></body></html>"))
        self.label_middle_z_det.setText(_translate("MainWindow", "1000"))
        self.label_top_z_det.setText(_translate("MainWindow", "2000"))
        self.label_bottom_z_det.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Detector:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Dectris Pilatus 1M"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Dectris Eiger 1M"))
from pyqtgraph import GraphicsLayoutWidget
