import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.body = Body(parent=self)
        self.setCentralWidget(self.body)

        # filling up a menu bar
        bar = self.menuBar()
        # File menu
        file_menu = bar.addMenu('File')
        close_action = QtWidgets.QAction('Close', self)
        file_menu.addAction(close_action)
        # use `connect` method to bind signals to desired behavior
        close_action.triggered.connect(self.close)

        self.show()


class Body(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QtWidgets.QGridLayout(self)


        # buttons
        refuel_button = QtWidgets.QPushButton("Nowe tankowanie")
        refuel_button.setIcon(QtGui.QIcon("img/refuel.png"))
        refuel_button.setMinimumHeight(25)
        refuel_button.clicked.connect(self.refuel)

        stats_button = QtWidgets.QPushButton("Statystyki")
        stats_button.setIcon(QtGui.QIcon("img/stats.png"))
        stats_button.setMinimumHeight(25)
        stats_button.clicked.connect(self.stats)


        history_button = QtWidgets.QPushButton("Historia")
        history_button.setIcon(QtGui.QIcon("img/history.png"))
        history_button.setMinimumHeight(25)

        # Initialize tab screen
        tabs = QtWidgets.QTabWidget()
        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()
        tabs.resize(300, 200)

        # Add tabs
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")



        # grid sets
        self.grid_layout.addWidget(tabs, 3,0)
        self.grid_layout.addWidget(refuel_button, 0,0)
        self.grid_layout.addWidget(stats_button, 0,1)
        self.grid_layout.addWidget(history_button, 0,2)

    def refuel(self):
        print("Nowe Tankowanie")

        fuel_label = QtWidgets.QLabel("Zatankowane paliwo: ")
        fuel_ledit = QtWidgets.QLineEdit()

        fuel_label2 = QtWidgets.QLabel("Cena za litr: ")
        fuel_ledit2 = QtWidgets.QLineEdit()

        fuel_label3 = QtWidgets.QLabel("Data tankowania: ")
        fuel_ledit3 = QtWidgets.QLineEdit()

        ok_button = QtWidgets.QPushButton("Dodaj")

        self.grid_layout.addWidget(fuel_label,1,0)
        self.grid_layout.addWidget(fuel_ledit,1,1)

        self.grid_layout.addWidget(fuel_label2,2,0)
        self.grid_layout.addWidget(fuel_ledit2,2,1)

        self.grid_layout.addWidget(fuel_label3,3,0)
        self.grid_layout.addWidget(fuel_ledit3,3,1)

        self.grid_layout.addWidget(ok_button, 4,1)

    def stats(self):

        stats_info = QtWidgets.QLabel("Informacja")

        self.grid_layout.addWidget(stats_info, 1,1)

        print("Statystyki")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # creating main window
    mw = Window()
    sys.exit(app.exec_())