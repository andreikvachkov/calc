# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desine.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QtCore.QSize(300, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/calculate_black_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_temp = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet("color: #888;")
        self.lbl_temp.setText("")
        self.lbl_temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_temp.setObjectName("lbl_temp")
        self.verticalLayout.addWidget(self.lbl_temp)
        self.le_entry = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy)
        self.le_entry.setStyleSheet("font-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(16)
        self.le_entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)
        self.le_entry.setObjectName("le_entry")
        self.verticalLayout.addWidget(self.le_entry)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 1, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mul.setObjectName("btn_mul")
        self.gridLayout.addWidget(self.btn_mul, 1, 4, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 3, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 3, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 0, 4, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 2, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 0, 1, 1, 1)
        self.btn_min = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)
        self.btn_min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_min.setObjectName("btn_min")
        self.gridLayout.addWidget(self.btn_min, 2, 4, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 1, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/backspace_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon1)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 0, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 3, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_plus.setIconSize(QtCore.QSize(16, 16))
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 3, 4, 1, 1)
        self.btn_mix = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mix.sizePolicy().hasHeightForWidth())
        self.btn_mix.setSizePolicy(sizePolicy)
        self.btn_mix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mix.setObjectName("btn_mix")
        self.gridLayout.addWidget(self.btn_mix, 4, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 2, 1, 1)
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy)
        self.btn_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 4, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        self.btn_eq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 4, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.le_entry.setText(_translate("MainWindow", "0"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_mul.setShortcut(_translate("MainWindow", "*"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_delete.setText(_translate("MainWindow", "C"))
        self.btn_delete.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_min.setText(_translate("MainWindow", "-"))
        self.btn_min.setShortcut(_translate("MainWindow", "-"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_clear.setText(_translate("MainWindow", "CE"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_mix.setText(_translate("MainWindow", "+/-"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_point.setText(_translate("MainWindow", "."))
        self.btn_point.setShortcut(_translate("MainWindow", "."))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.btn_eq.setShortcut(_translate("MainWindow", "="))
import file_rc
