from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from game import *


class Gra(QWidget):
    def __init__(self, rodzic=None):
        super().__init__(rodzic)
        self.interfejs()

    def interfejs(self):

        login = QLabel("Login: ",self)
        haslo = QLabel("Hasło: ",self)

        self.show_id = QLabel("ID: ",self)
        self.show_name = QLabel("Nick: ",self)
        self.show_metal = QLabel("Żelazo: ",self)

        self.details_game = QTextEdit()
        self.login_in = QLineEdit()
        self.haslo_in = QLineEdit()

        przycisk = QPushButton("Zaloguj się",self)


        uklad = QGridLayout()
        uklad.addWidget(login, 0, 0)
        uklad.addWidget(haslo, 1, 0)
        uklad.addWidget(self.show_id, 3, 0)
        uklad.addWidget(self.show_name, 3, 1)
        uklad.addWidget(self.show_metal, 3, 2)


        uklad.addWidget(self.login_in, 0, 1)
        uklad.addWidget(self.haslo_in, 1, 1)
        uklad.addWidget(przycisk, 2, 0)
        uklad.addWidget(self.details_game, 4, 1, 1, 1)


        przycisk.clicked.connect(self.dzialanie)

        self.setLayout(uklad)
        self.setGeometry(20,20,400,200)
        self.setWindowTitle("Gra symulacyjna")
        self.show()

    def dzialanie(self):

        pole1 = str(self.login_in.text())
        pole2 = str(self.haslo_in.text())

        login = Login(pole1, pole2)
        sur = Surowce("1")
        print(sur.name)


        self.details_game.setText(read_statistics(login.log()))
        self.show_id.setText(f'ID: {login.log()}')







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Gra()
    sys.exit(app.exec_())