"""
Database handling functionality.
"""

import pandas as pd

class Database:

    def __init__(self):
        """
        Initialize all necessary variables.
        """
        self.dataBaseFilePath : str | None = None
        self.configFilePath : str | None = None
        self.dataBaseByMonth : dict[str, dict[str, pd.DataFrame]] = {}

    def OpenDataBaseFileAndSort(self, filePath : str):

        data = pd.read_csv(filePath, sep=';')

        for val in data['Buchungstag']:
            print(val)


        