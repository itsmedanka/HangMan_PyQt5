from PyQt5 import QtCore, QtGui, QtWidgets
from hangmansecond import Ui_HangManSecondWindow
from hangmanthird import Ui_HangManThirdWindow

class Ui_HangMan_MainScreen(object):
    def setupUi(self, HangMan_MainScreen):
        HangMan_MainScreen.setObjectName("HangMan_MainScreen")
        HangMan_MainScreen.resize(397, 800)
        HangMan_MainScreen.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        HangMan_MainScreen.setStyleSheet("background-color : gray;")
        self.centralwidget = QtWidgets.QWidget(HangMan_MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.TooEasy = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : Ui_HangManThirdWindow().setupUi(HangMan_MainScreen))
        self.TooEasy.setGeometry(QtCore.QRect(100,200,171,51))
        self.TooEasy.setObjectName("TooEasy")
        self.TooHard = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: Ui_HangManSecondWindow().setupUi(HangMan_MainScreen))
        self.TooHard.setGeometry(QtCore.QRect(100, 300, 171, 51))
        self.TooHard.setObjectName("TooHard")
        self.Exit = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: exit())
        self.Exit.setGeometry(QtCore.QRect(100, 400, 171, 51))
        self.Exit.setObjectName("Exit")
        self.HangManFrontScreenLabel = QtWidgets.QLabel(self.centralwidget)
        self.HangManFrontScreenLabel.setGeometry(QtCore.QRect(0, 0, 397, 131))
        font = QtGui.QFont()
        font.setFamily("Nakula")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.HangManFrontScreenLabel.setFont(font)
        self.HangManFrontScreenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HangManFrontScreenLabel.setObjectName("HangManFrontScreenLabel")
        HangMan_MainScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(HangMan_MainScreen)
        QtCore.QMetaObject.connectSlotsByName(HangMan_MainScreen)

    def retranslateUi(self, HangMan_MainScreen):
        _translate = QtCore.QCoreApplication.translate
        HangMan_MainScreen.setWindowTitle(_translate("HangMan_MainScreen", "Hangman"))
        self.TooHard.setText(_translate("HangMan_MainScreen", "TooHard"))
        self.TooEasy.setText(_translate("HangMan_MainScreen","Too Easy"))
        self.Exit.setText(_translate("HangMan_MainScreen", "I am Coward"))
        self.HangManFrontScreenLabel.setText(_translate("HangMan_MainScreen", "HangMan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HangMan_MainScreen = QtWidgets.QMainWindow()
    ui = Ui_HangMan_MainScreen()
    ui.setupUi(HangMan_MainScreen)
    HangMan_MainScreen.show()
    sys.exit(app.exec_())
