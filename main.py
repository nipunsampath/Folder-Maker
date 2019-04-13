from FolderOperations import FolderOperations
from GUI.mainUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui,QtCore

import sys


class Main(QtWidgets.QMainWindow):
    PerSeason = 1
    PerEpisode = 2
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowIcon(QtGui.QIcon("folder.png"))
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.openFolderPath.clicked.connect(self.openFolderSelectDialog)
        self.ui.createSeries.clicked.connect(self.createSeriesDirectory)
        self.ui.perEpisodeRb.toggled.connect(self.radioButtonToggled)
        self.ui.perSeasonRb.toggled.connect(self.radioButtonToggled)
        self.onlyInt = QtGui.QIntValidator()
        # self.ui.numberOfEpisodes.textChanged.connect(self.check_state)
        # self.ui.numberOfEpisodes.emit(self.ui.numberOfEpisodes.text())
        self.ui.numberOfEpisodes.setValidator(self.onlyInt)
        self.ui.numberOfSeasons.setValidator(self.onlyInt)

    def openFolderSelectDialog(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Path", "",
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        self.ui.folderPathLineEdit.setText(fileName)

    def radioButtonToggled(self):
        if self.ui.perEpisodeRb.isChecked():
            self.tvSeriesMode = Main.PerEpisode
        elif self.ui.perSeasonRb.isChecked():
            self.tvSeriesMode = Main.PerSeason

    def checkForEmptyLineEdits(self,arr):
        """Takes an array of elements and check returns whether they are empty"""
        for element in arr:
            if element.text() == "":
                return False
        return True

    def createSeriesDirectory(self):
        path = self.ui.folderPathLineEdit.text()
        seriesName = self.ui.seriesName.text()
        numberOfSeasons = self.ui.numberOfSeasons.text()
        numberOfEpisodes = self.ui.numberOfEpisodes.text()
        msgBox = QtWidgets.QMessageBox()
        if path != "" and seriesName != "" and numberOfEpisodes != "" and numberOfSeasons != "":

            folderOps = FolderOperations(seriesName, int(numberOfSeasons), int(numberOfEpisodes), path)
            if self.tvSeriesMode == Main.PerEpisode:
                requestCode = folderOps.make_series()
            elif self.tvSeriesMode == Main.PerSeason:
                requestCode = folderOps.make_series_without_episode_dir()

            if requestCode == FolderOperations.SUCCESS:
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText('Directories Created!')
                msgBox.setWindowTitle("Success")
                msgBox.exec_()
            else:
                msgBox.setIcon(QtWidgets.QMessageBox.Critical)
                msgBox.setText('Directory already Exists')
                msgBox.setWindowTitle("Error")
                msgBox.exec_()

        else:
            msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            msgBox.setText('Check the inputs')
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
