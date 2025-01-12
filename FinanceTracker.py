"""
This is the main file of the Finance Tracker.
It sets up the GUI, initializes all necessary modules and executes the 
application.
"""

import sys
from PyQt6 import QtWidgets
import GUI.FinanceTrackerMainUI as UI


class FinanceTrackerWindow(QtWidgets.QMainWindow, UI.Ui_mainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def openConfigFileDialog(self):
        print("Test")

    def openDataBaseFileDialog(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open Database file", "" ,"Data Files (*.csv))")
        print(fileName)

if __name__ == "__main__":

    ftApp = QtWidgets.QApplication(sys.argv)
    mainWindow = FinanceTrackerWindow()


    mainWindow.show()

    ftApp.exec()


