# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/snimki/icons8_estimate_96_H72_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 398, 280))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 380, 180))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.text = QtWidgets.QLabel(self.about)
        self.text.setGeometry(QtCore.QRect(90, 10, 260, 41))
        self.text.setObjectName("text")
        self.pyimage = QtWidgets.QLabel(self.about)
        self.pyimage.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pyimage.setText("")
        self.pyimage.setPixmap(QtGui.QPixmap(":/images/snimki/icons8-color-96.png"))
        self.pyimage.setScaledContents(True)
        self.pyimage.setObjectName("pyimage")
        self.qtimage = QtWidgets.QLabel(self.about)
        self.qtimage.setGeometry(QtCore.QRect(10, 80, 70, 70))
        self.qtimage.setText("")
        self.qtimage.setPixmap(QtGui.QPixmap(":/images/snimki/kisspng-qt-creator-qt-quick-the-qt-company-posted-write-5b1b6b4ccbb114.1843493915285235968343.png"))
        self.qtimage.setScaledContents(True)
        self.qtimage.setObjectName("qtimage")
        self.line = QtWidgets.QFrame(self.about)
        self.line.setGeometry(QtCore.QRect(90, 55, 90, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.piton = QtWidgets.QLabel(self.about)
        self.piton.setGeometry(QtCore.QRect(90, 70, 70, 16))
        self.piton.setObjectName("piton")
        self.picute = QtWidgets.QLabel(self.about)
        self.picute.setGeometry(QtCore.QRect(90, 90, 60, 16))
        self.picute.setObjectName("picute")
        self.line_2 = QtWidgets.QFrame(self.about)
        self.line_2.setGeometry(QtCore.QRect(90, 105, 90, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.about, "")
        self.license = QtWidgets.QWidget()
        self.license.setObjectName("license")
        self.licensetext = QtWidgets.QTextEdit(self.license)
        self.licensetext.setEnabled(True)
        self.licensetext.setGeometry(QtCore.QRect(10, 10, 350, 130))
        self.licensetext.setReadOnly(True)
        self.licensetext.setObjectName("licensetext")
        self.tabWidget.addTab(self.license, "")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 20, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 60, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/snimki/icons8_estimate_96_H72_icon.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About qExchanger"))
        self.text.setText(_translate("Dialog", "qExchanger is CC, written on Python with PyQt5.\n"
"\n"
"For your convenience, the program updates daily."))
        self.piton.setText(_translate("Dialog", "Python 3.7.3"))
        self.picute.setText(_translate("Dialog", "PyQt 5.12.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("Dialog", "About"))
        self.licensetext.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/snimki/gplv3-with-text-136x68.png\" width=\"70\" height=\"40\" />   <span style=\" font-size:10pt;\"> </span><span style=\" font-size:8pt;\">This program is licensed under GNU GPLv3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    This program is free software: you can redistribute it and/or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    the Free Software Foundation, either version 3 of the License, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    (at your option) any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    You should have received a copy of the GNU General Public License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:8pt;\">    along with this program.  If not, see &lt;https://www.gnu.org/licenses/&gt;.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.license), _translate("Dialog", "License"))
        self.label.setText(_translate("Dialog", "qExchanger"))


import icons_rc
