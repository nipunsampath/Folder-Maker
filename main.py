from FolderOperations import FolderOperations
from GUI.mainUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui

import sys


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.openFolderPath.clicked.connect(self.openFolderSelectDialog)
        self.ui.createSeries.clicked.connect(self.createSeriesDirectory)
        self.onlyInt = QtGui.QIntValidator()
        # self.ui.numberOfEpisodes.textChanged.connect(self.check_state)
        # self.ui.numberOfEpisodes.emit(self.ui.numberOfEpisodes.text())
        self.ui.numberOfEpisodes.setValidator(self.onlyInt)
        self.ui.numberOfSeasons.setValidator(self.onlyInt)

    def openFolderSelectDialog(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Path", "",
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        self.ui.folderPathLineEdit.setText(fileName)

    def createSeriesDirectory(self):
        path = self.ui.folderPathLineEdit.text()
        seriesName = self.ui.seriesName.text()
        numberOfSeasons = int(self.ui.numberOfSeasons.text())
        numberOfEpisodes = int(self.ui.numberOfEpisodes.text())

        folderOps = FolderOperations(seriesName, numberOfSeasons, numberOfEpisodes, path)
        requestCode = folderOps.make_series()

        msgBox = QtWidgets.QMessageBox()
        if requestCode == FolderOperations.SUCCESS:
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText('Directories Created!')
            msgBox.setWindowTitle("Success")
            msgBox.exec_()
        else:
            msgBox.setIcon(QtWidgets.QMessageBox.Critical)

            msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            msgBox.setText('Directory already Exists')
            msgBox.setWindowTitle("Error")
            msgBox.exec_()

    # To DO
    # def check_state(self, *args, **kwargs):
    #     sender = self.sender()
    #     validator = sender.validator()
    #     state = validator.validate(sender.text(), 0)[0]
    #     if state == QtGui.QValidator.Acceptable:
    #         color = '#c4df9b'  # green
    #     elif state == QtGui.QValidator.Intermediate:
    #         color = '#fff79a'  # yellow
    #     else:
    #         color = '#f6989d'  # red
    #     sender.setStyleSheet('QLineEdit { background-color: %s }' % color)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    application = Main()

    application.show()

    sys.exit(app.exec())
