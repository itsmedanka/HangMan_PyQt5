from PyQt5 import QtCore, QtGui, QtWidgets
import random
from PyQt5.QtGui import QPixmap



class Ui_HangManSecondWindow(object):
    def setupUi(self, HangManSecondWindow):
        HangManSecondWindow.setObjectName("HangManSecondWindow")
        HangManSecondWindow.resize(397, 800)
        HangManSecondWindow.setStyleSheet("background-color : grey;")
        HangManSecondWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.centralwidget = QtWidgets.QWidget(HangManSecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        self.CannyImages = QtWidgets.QLabel(self.centralwidget)
        self.CannyImages.setGeometry(QtCore.QRect(195, 0, 200, 181+150))
        self.CannyImages.setObjectName("CannyImages")
        self.CannyImages.setFont(font)
        self.HangingImages = QtWidgets.QLabel(self.centralwidget)
        self.HangingImages.setGeometry(QtCore.QRect(0, 0, 190, 181+150))
        self.HangingImages.setObjectName("HangingImages")
        self.B = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("B"))
        self.B.setGeometry(QtCore.QRect(70, 310+150, 50, 50))
        self.B.setObjectName("B")
        self.D = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("D"))
        self.D.setGeometry(QtCore.QRect(210, 310+150, 50, 50))
        self.D.setObjectName("D")
        self.U = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("U"))
        self.U.setGeometry(QtCore.QRect(130, 490+150, 50, 50))
        self.U.setObjectName("U")
        self.N = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("N"))
        self.N.setGeometry(QtCore.QRect(70, 430+150, 50, 50))
        self.N.setObjectName("N")
        self.S = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("S"))
        self.S.setGeometry(QtCore.QRect(10, 490+150, 50, 50))
        self.S.setObjectName("S")
        self.C = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("C"))
        self.C.setGeometry(QtCore.QRect(130, 310+150, 50, 50))
        self.C.setObjectName("C")
        self.A = QtWidgets.QToolButton(self.centralwidget, clicked = lambda: self.HangManButtons("A"))
        self.A.setGeometry(QtCore.QRect(10, 310+150, 50, 50))
        self.A.setObjectName("A")
        self.P = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("P"))
        self.P.setGeometry(QtCore.QRect(210, 430+150, 50, 50))
        self.P.setObjectName("P")
        self.Q = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("Q"))
        self.Q.setGeometry(QtCore.QRect(270, 430+150, 50, 50))
        self.Q.setObjectName("Q")
        self.O = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("O"))
        self.O.setGeometry(QtCore.QRect(130, 430+150, 50, 50))
        self.O.setObjectName("O")
        self.V = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("V"))
        self.V.setGeometry(QtCore.QRect(210, 490+150, 50, 50))
        self.V.setObjectName("V")
        self.W = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("W"))
        self.W.setGeometry(QtCore.QRect(270, 490+150, 50, 50))
        self.W.setObjectName("W")
        self.H = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("H"))
        self.H.setGeometry(QtCore.QRect(70, 370+150, 50, 50))
        self.H.setObjectName("H")
        self.L = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("L"))
        self.L.setGeometry(QtCore.QRect(330, 370+150, 50, 50))
        self.L.setObjectName("L")
        self.R = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("R"))
        self.R.setGeometry(QtCore.QRect(330, 430+150, 50, 50))
        self.R.setObjectName("R")
        self.X = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("X"))
        self.X.setGeometry(QtCore.QRect(330, 490+150, 50, 50))
        self.X.setObjectName("X")
        self.Z = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("Z"))
        self.Z.setGeometry(QtCore.QRect(210, 700, 50, 50))
        self.Z.setObjectName("Z")
        self.Y = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("Y"))
        self.Y.setGeometry(QtCore.QRect(130, 700, 50, 50))
        self.Y.setObjectName("Y")
        self.K = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("K"))
        self.K.setGeometry(QtCore.QRect(270, 370+150, 50, 50))
        self.K.setObjectName("K")
        self.M = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("M"))
        self.M.setGeometry(QtCore.QRect(10, 430+150, 50, 50))
        self.M.setObjectName("M")
        self.F = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("F"))
        self.F.setGeometry(QtCore.QRect(330, 310+150, 50, 50))
        self.F.setObjectName("F")
        self.E = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("E"))
        self.E.setGeometry(QtCore.QRect(270, 310+150, 50, 50))
        self.E.setObjectName("E")
        self.G = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("G"))
        self.G.setGeometry(QtCore.QRect(10, 370+150, 50, 50))
        self.G.setObjectName("G")
        self.T = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("T"))
        self.T.setGeometry(QtCore.QRect(70, 490+150, 50, 50))
        self.T.setObjectName("T")
        self.I = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("I"))
        self.I.setGeometry(QtCore.QRect(130, 370+150, 50, 50))
        self.I.setObjectName("I")
        self.J = QtWidgets.QToolButton(self.centralwidget,clicked = lambda: self.HangManButtons("J"))
        self.J.setGeometry(QtCore.QRect(210, 370+150, 50, 50))
        self.J.setObjectName("J")
        self.TextHangMan = QtWidgets.QLabel(self.centralwidget)
        self.TextHangMan.setGeometry(QtCore.QRect(0, 181+150, 397, 100))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.TextHangMan.setFont(font)
        self.TextHangMan.setText("")
        self.TextHangMan.setAlignment(QtCore.Qt.AlignCenter)
        self.TextHangMan.setObjectName("TextHangMan")
        HangManSecondWindow.setCentralWidget(self.centralwidget)
        self.Starting()
        self.retranslateUi(HangManSecondWindow)
        QtCore.QMetaObject.connectSlotsByName(HangManSecondWindow)
        print("hello")
        self.count = 0


    def Starting(self):
        with open('Words.txt','r') as f:
            words = f.readlines()
        self.word = random.choice(words)
        self.word = self.word.strip()
        self.dashtext = []
        self.dashes = []
        self.showingdashes = ""
        for i in range(len(self.word)):
            self.dashtext.append(self.word[i])
            self.dashes.append("__ ")
            self.showingdashes = self.showingdashes + "__ "
        self.TextHangMan.setText(self.showingdashes)


    def HangManButtons(self,letter):
        if letter in self.word:
            for n, i in enumerate(self.dashtext):
                if i == letter:
                    self.dashes[n] = letter
            self.answers = ""
            for i in self.dashes:
                self.answers = self.answers + i

            for i in self.answers:
                if i.isalpha() == True:
                    self.TextHangMan.setText("YOU WON!")
                else:
                    self.TextHangMan.setText(self.answers)

        if letter not in self.word:
            self.count = self.count + 1
            if self.count == 1:
                pixmap = QPixmap('hangman0.png')
                self.HangingImages.setPixmap(pixmap)
                self.CannyImages.setText(f'Only {7-int(self.count)} chances left')
                # pixelmap = QPixmap('home/yash/Downloads/Canny0.png')
                # self.CannyImages.setPixmap(pixelmap)
            if self.count == 2:
                pixmap = QPixmap('hangman1.png')
                self.HangingImages.setPixmap(pixmap)
                self.CannyImages.setText(f'Only {7 - int(self.count)} chances left')
                # pixmap = QPixmap('home/yash/Downloads/Canny1.png')
                # self.CannyImages.setPixmap(pixmap)
            if self.count == 3:
                pixmap = QPixmap('hangman2.png')
                self.HangingImages.setPixmap(pixmap)
                self.CannyImages.setText(f'Only {7 - int(self.count)} chances left')
                # pixmap = QPixmap('home/yash/Downloads/Canny2.png')
                # self.CannyImages.setPixmap(pixmap)
            if self.count == 4:
                pixmap = QPixmap('hangman3.png')
                self.HangingImages.setPixmap(pixmap)
                self.CannyImages.setText(f'Only {7 - int(self.count)} chances left')
                # pixmap = QPixmap('home/yash/Downloads/Canny3.png')
                # self.CannyImages.setPixmap(pixmap)
            if self.count == 5:
                pixmap = QPixmap('hangman4.png')
                self.HangingImages.setPixmap(pixmap)
                self.CannyImages.setText(f'Only {7 - int(self.count)} chances left')
                # pixmap = QPixmap('home/yash/Downloads/Canny4.png')
                # self.CannyImages.setPixmap(pixmap)
            if self.count == 6:
                pixmap = QPixmap('hangman5.png')
                self.HangingImages.setPixmap(pixmap)
                self.CannyImages.setText(f'Only {7- int(self.count)} chances left')
                # pixmap = QPixmap('home/yash/Downloads/Canny5.png')
                # self.CannyImages.setPixmap(pixmap)
            if self.count == 7:
                pixmap = QPixmap('hangman6.png')
                self.HangingImages.setPixmap(pixmap)
                font = QtGui.QFont()
                font.setFamily("Ubuntu Condensed")
                font.setPointSize(50)
                font.setBold(True)
                self.CannyImages.setFont(font)
                self.CannyImages.setText('😭')
                # pixmap = QPixmap('home/yash/Downloads/Canny6.png')
                # self.CannyImages.setPixmap(pixmap)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                self.TextHangMan.setFont(font)
                self.TextHangMan.setText(f"YOU LOST!,the word is {self.word}")

    def retranslateUi(self, HangManSecondWindow):
        _translate = QtCore.QCoreApplication.translate
        HangManSecondWindow.setWindowTitle(_translate("HangManSecondWindow", "Hangman"))
        self.CannyImages.setText(_translate("HangManSecondWindow", "Chances"))
        self.HangingImages.setText(_translate("HangManSecondWindow", "Find the Word!"))
        self.B.setText(_translate("HangManSecondWindow", "B"))
        self.D.setText(_translate("HangManSecondWindow", "D"))
        self.U.setText(_translate("HangManSecondWindow", "U"))
        self.N.setText(_translate("HangManSecondWindow", "N"))
        self.S.setText(_translate("HangManSecondWindow", "S"))
        self.C.setText(_translate("HangManSecondWindow", "C"))
        self.A.setText(_translate("HangManSecondWindow", "A"))
        self.P.setText(_translate("HangManSecondWindow", "P"))
        self.Q.setText(_translate("HangManSecondWindow", "Q"))
        self.O.setText(_translate("HangManSecondWindow", "O"))
        self.V.setText(_translate("HangManSecondWindow", "V"))
        self.W.setText(_translate("HangManSecondWindow", "W"))
        self.H.setText(_translate("HangManSecondWindow", "H"))
        self.L.setText(_translate("HangManSecondWindow", "L"))
        self.R.setText(_translate("HangManSecondWindow", "R"))
        self.X.setText(_translate("HangManSecondWindow", "X"))
        self.Z.setText(_translate("HangManSecondWindow", "Z"))
        self.Y.setText(_translate("HangManSecondWindow", "Y"))
        self.K.setText(_translate("HangManSecondWindow", "K"))
        self.M.setText(_translate("HangManSecondWindow", "M"))
        self.F.setText(_translate("HangManSecondWindow", "F"))
        self.E.setText(_translate("HangManSecondWindow", "E"))
        self.G.setText(_translate("HangManSecondWindow", "G"))
        self.T.setText(_translate("HangManSecondWindow", "T"))
        self.I.setText(_translate("HangManSecondWindow", "I"))
        self.J.setText(_translate("HangManSecondWindow", "J"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HangManSecondWindow = QtWidgets.QMainWindow()
    ui = Ui_HangManSecondWindow()
    ui.setupUi(HangManSecondWindow)
    HangManSecondWindow.show()
    sys.exit(app.exec_())
