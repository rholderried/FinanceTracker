"""
This is the main file of the Finance Tracker.
It sets up the GUI, initializes all necessary modules and executes the 
application.
"""

import sys
from PyQt6 import QtWidgets
import GUI.FinanceTrackerMainUI as UI
import backend.Database as db

class FinanceTrackerWindow(QtWidgets.QMainWindow, UI.Ui_mainWindow):
    def __init__(self, parent, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.parent = parent

    def openConfigFileDialog(self):
        print("Test")

    def openDataBaseFileDialog(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open Database file", "" ,"Data Files (*.csv))")
        self.parent.database.OpenDataBaseFileAndSort(filePath = fileName[0])


class FinanceTracker(QtWidgets.QApplication):

    def __init__(self, argv):

        QtWidgets.QApplication.__init__(self, argv)

        self.mainWindow = FinanceTrackerWindow(parent = self)
        self.database = db.Database()
        self.mainWindow.show()


if __name__ == "__main__":

    ftApp = FinanceTracker(sys.argv)
    
    ftApp.exec()



