from FolderOperations import FolderOperations
from GUI.mainUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui

import sys


class Main(QtWidgets.QMainWindow):
    PerSeason = 1
    PerEpisode = 2

    def __init__(self):
        super(Main, self).__init__()
        self.setWindowIcon(QtGui.QIcon("folder.png"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolBox.setCurrentIndex(1)
        self.tvSeriesMode = Main.PerEpisode
        # Connecting graphical elements with respective functions in TV series page
        self.ui.openFolderPath.clicked.connect(self.openFolderSelectDialog)
        self.ui.createSeries.clicked.connect(self.createSeriesDirectory)
        self.ui.perEpisodeRb.toggled.connect(self.radioButtonToggled)
        self.ui.perSeasonRb.toggled.connect(self.radioButtonToggled)

        self.onlyInt = QtGui.QIntValidator()
        self.ui.numberOfEpisodes.setValidator(self.onlyInt)
        self.ui.numberOfSeasons.setValidator(self.onlyInt)

        # Connecting graphical elements with respective functions in Movies page
        self.ui.addButton.clicked.connect(self.addMovie)
        self.ui.editButton.clicked.connect(self.editMovie)
        self.ui.removeButton.clicked.connect(self.delMovie)
        self.ui.createMoviesButton.clicked.connect(self.createMovieDirectories)

    def openFolderSelectDialog(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Path", "",
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        self.ui.folderPathLineEdit.setText(fileName)

    def radioButtonToggled(self):
        if self.ui.perEpisodeRb.isChecked():
            self.tvSeriesMode = Main.PerEpisode
        elif self.ui.perSeasonRb.isChecked():
            self.tvSeriesMode = Main.PerSeason

    def checkForEmptyLineEdits(self, arr):
        """Takes an array of elements and check returns whether they are empty"""
        for element in arr:
            if element.text() == "":
                return False
        return True

    def addMovie(self):
        row = self.ui.listWidget.currentRow()
        movie, ok = QtWidgets.QInputDialog.getText(self, "Add Movie", "Movie Name: ")

        if ok and movie is not None:
            self.ui.listWidget.insertItem(row, movie)

    def editMovie(self):
        row = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(row)

        if item is not None:
            movie, ok = QtWidgets.QInputDialog.getText(self, "Edit Movie", "Movie Name: ", QtWidgets.QLineEdit.Normal,
                                                       item.text())
            if movie and ok is not None:
                item.setText(movie)

    def delMovie(self):
        row = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(row)

        if item is None:
            return
        confirm = QtWidgets.QMessageBox.question(self, "Remove Movie", "Do you want to remove " + str(item.text()),
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            item = self.ui.listWidget.takeItem(row)
            del item

    def createSeriesDirectory(self):
        path = self.ui.folderPathLineEdit.text()
        seriesName = self.ui.seriesName.text()
        numberOfSeasons = self.ui.numberOfSeasons.text()
        numberOfEpisodes = self.ui.numberOfEpisodes.text()
        msgBox = QtWidgets.QMessageBox()
        requestCode = 0

        if path != "" and seriesName != "" and numberOfEpisodes != "" and numberOfSeasons != "":

            folderOps = FolderOperations(seriesName, int(numberOfSeasons), int(numberOfEpisodes), path)
            if self.tvSeriesMode == Main.PerEpisode:
                requestCode = folderOps.make_series()
            elif self.tvSeriesMode == Main.PerSeason:
                requestCode = folderOps.make_series_without_episode_dir()

            if requestCode == FolderOperations.SUCCESS:
                self.createSuccessMsgBox(msgBox)
            else:
                self.createOSERRORmsgBox(msgBox)

        else:
            self.inputErrorMsgBox(msgBox)

    def createOSERRORmsgBox(self, msgBox):
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setText('Directory already Exists')
        msgBox.setWindowTitle("Error")
        msgBox.exec_()

    def createSuccessMsgBox(self, msgBox):
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText('Directories Created!')
        msgBox.setWindowTitle("Success")
        msgBox.exec_()

    def createMovieDirectories(self):

        path = self.ui.folderPathLineEdit.text()
        msgBox = QtWidgets.QMessageBox()

        if path != "" and self.ui.listWidget.count() != 0:
            movies = list(str(self.ui.listWidget.item(i).text()) for i in range(self.ui.listWidget.count()))
            folderOps = FolderOperations(None, None, None, path)
            requestCode = folderOps.make_movie_directories(movies, self.ui.subsChecBox.isChecked())

            if requestCode == FolderOperations.SUCCESS:
                self.createSuccessMsgBox(msgBox)
            else:
                self.createOSERRORmsgBox(msgBox)
        else:
            self.inputErrorMsgBox(msgBox)

    def inputErrorMsgBox(self, msgBox):
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setText('Check the inputs')
        msgBox.setWindowTitle("Error")
        msgBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    application = Main()

    application.show()

    sys.exit(app.exec())
