from kid import kid_neuro
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
qt_main_file = 'untitled.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_main_file)


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_result)

    def get_result(self):
        epoch = self.lineEdit.text()
        lr = self.lineEdit_2.text()
        accur = self.lineEdit_3.text()
        centimtre=self.lineEdit_4.text()
        inches = self.lineEdit_5.text()        
        result = kid_neuro(epoch, lr, accur,inches,centimtre)
        self.textEdit.append('Результат составил '+ str(result))  

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())
