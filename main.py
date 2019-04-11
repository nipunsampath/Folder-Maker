from FolderOperations import FolderOperations
from GUI.mainUI import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui

import sys


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.openFolderPath.clicked.connect(self.openFolderSelectDialog)
        self.ui.createSeries.clicked.connect(self.createSeriesDirectory)

    def openFolderSelectDialog(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Path","", QtWidgets.QFileDialog.ShowDirsOnly)
        self.ui.folderPathLineEdit.setText(fileName)

    def createSeriesDirectory(self):
        path = self.ui.folderPathLineEdit.text()
        seriesName = self.ui.seriesName.text()
        numberOfSeasons = self.ui.numberOfSeasons.text()
        numberOfEpisodes = self.ui.numberOfEpisodes.text()
        folderOps = FolderOperations(seriesName,numberOfSeasons,numberOfEpisodes,path)
        folderOps.make_series()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    application = Main()

    application.show()

    sys.exit(app.exec())
