# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NNTF import predictionfun

class Ui_Dialog(object):
    fileName=''
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(474, 325)
        self.selectig_2 = QtWidgets.QPushButton(Dialog)
        self.selectig_2.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.selectig_2.setFont(font)
        self.selectig_2.setObjectName("selectig_2")
        self.imglab = QtWidgets.QLabel(Dialog)
        self.imglab.setGeometry(QtCore.QRect(170, 20, 281, 281))
        self.imglab.setFrameShape(QtWidgets.QFrame.Box)
        self.imglab.setText("")
        self.imglab.setObjectName("imglab")
        self.prediction = QtWidgets.QPushButton(Dialog)
        self.prediction.setGeometry(QtCore.QRect(20, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.prediction.setFont(font)
        self.prediction.setObjectName("prediction")
        self.nub = QtWidgets.QTextEdit(Dialog)
        self.nub.setGeometry(QtCore.QRect(40, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nub.setFont(font)
        self.nub.setObjectName("nub")





        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.selectig_2.clicked.connect(self.setImage)
        print('hhhhhhhhhhhhhhhh')
        self.prediction.clicked.connect(self.addItem)
        print('jjjjjjjjjjjjj')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chaima"))
        self.selectig_2.setText(_translate("Dialog", "Input image"))
        self.prediction.setText(_translate("Dialog", "Recognized digit"))

    def setImage(self ):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if self.fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(self.fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imglab.width(), self.imglab.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imglab.setPixmap(pixmap) # Set the pixmap onto the label
            self.imglab.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
            print(type(self.fileName))


    def addItem(self  ):

        if self.fileName!='':
            print('ddddd')
            nb = predictionfun(self.fileName)
            self.nub.setText(str(nb))  # Add the value we got to the list





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

