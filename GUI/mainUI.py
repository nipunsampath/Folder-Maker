# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Python\Folder Maker\GUI\main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 384)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folderPathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.folderPathLineEdit.setGeometry(QtCore.QRect(110, 20, 581, 22))
        self.folderPathLineEdit.setObjectName("folderPathLineEdit")
        self.openFolderPath = QtWidgets.QPushButton(self.centralwidget)
        self.openFolderPath.setGeometry(QtCore.QRect(10, 17, 93, 28))
        self.openFolderPath.setObjectName("openFolderPath")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 70, 671, 271))
        self.toolBox.setObjectName("toolBox")
        self.movies = QtWidgets.QWidget()
        self.movies.setGeometry(QtCore.QRect(0, 0, 671, 209))
        self.movies.setObjectName("movies")
        self.addButton = QtWidgets.QPushButton(self.movies)
        self.addButton.setGeometry(QtCore.QRect(550, 30, 93, 28))
        self.addButton.setObjectName("addButton")
        self.createMoviesButton = QtWidgets.QPushButton(self.movies)
        self.createMoviesButton.setGeometry(QtCore.QRect(550, 150, 93, 28))
        self.createMoviesButton.setObjectName("createMoviesButton")
        self.removeButton = QtWidgets.QPushButton(self.movies)
        self.removeButton.setGeometry(QtCore.QRect(550, 110, 93, 28))
        self.removeButton.setObjectName("removeButton")
        self.editButton = QtWidgets.QPushButton(self.movies)
        self.editButton.setGeometry(QtCore.QRect(550, 70, 93, 28))
        self.editButton.setObjectName("editButton")
        self.listWidget = QtWidgets.QListWidget(self.movies)
        self.listWidget.setGeometry(QtCore.QRect(57, 5, 451, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.subsChecBox = QtWidgets.QCheckBox(self.movies)
        self.subsChecBox.setGeometry(QtCore.QRect(550, 0, 81, 20))
        self.subsChecBox.setObjectName("subsChecBox")
        self.toolBox.addItem(self.movies, "")
        self.tvShow = QtWidgets.QWidget()
        self.tvShow.setGeometry(QtCore.QRect(0, 0, 671, 209))
        self.tvShow.setObjectName("tvShow")
        self.seriesName = QtWidgets.QLineEdit(self.tvShow)
        self.seriesName.setGeometry(QtCore.QRect(230, 20, 241, 22))
        self.seriesName.setObjectName("seriesName")
        self.label = QtWidgets.QLabel(self.tvShow)
        self.label.setGeometry(QtCore.QRect(140, 20, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tvShow)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 121, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.numberOfSeasons = QtWidgets.QLineEdit(self.tvShow)
        self.numberOfSeasons.setGeometry(QtCore.QRect(230, 60, 241, 22))
        self.numberOfSeasons.setObjectName("numberOfSeasons")
        self.numberOfEpisodes = QtWidgets.QLineEdit(self.tvShow)
        self.numberOfEpisodes.setGeometry(QtCore.QRect(230, 100, 241, 22))
        self.numberOfEpisodes.setObjectName("numberOfEpisodes")
        self.label_3 = QtWidgets.QLabel(self.tvShow)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 121, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tvShow)
        self.label_4.setGeometry(QtCore.QRect(100, 140, 121, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.createSeries = QtWidgets.QPushButton(self.tvShow)
        self.createSeries.setGeometry(QtCore.QRect(530, 70, 93, 28))
        self.createSeries.setObjectName("createSeries")
        self.groupBox = QtWidgets.QGroupBox(self.tvShow)
        self.groupBox.setGeometry(QtCore.QRect(230, 129, 241, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.perEpisodeRb = QtWidgets.QRadioButton(self.groupBox)
        self.perEpisodeRb.setGeometry(QtCore.QRect(10, 10, 221, 20))
        self.perEpisodeRb.setChecked(True)
        self.perEpisodeRb.setObjectName("perEpisodeRb")
        self.perSeasonRb = QtWidgets.QRadioButton(self.groupBox)
        self.perSeasonRb.setGeometry(QtCore.QRect(10, 40, 221, 20))
        self.perSeasonRb.setObjectName("perSeasonRb")
        self.toolBox.addItem(self.tvShow, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Folder Maker"))
        self.openFolderPath.setText(_translate("MainWindow", "Folder Path"))
        self.addButton.setText(_translate("MainWindow", "Add "))
        self.addButton.setShortcut(_translate("MainWindow", "A"))
        self.createMoviesButton.setText(_translate("MainWindow", "Create "))
        self.createMoviesButton.setShortcut(_translate("MainWindow", "C"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.removeButton.setShortcut(_translate("MainWindow", "R"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.editButton.setShortcut(_translate("MainWindow", "E"))
        self.subsChecBox.setText(_translate("MainWindow", "Subtitles"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.movies), _translate("MainWindow", "Movies"))
        self.label.setText(_translate("MainWindow", "Series Name"))
        self.label_2.setText(_translate("MainWindow", "Number of Seasons"))
        self.label_3.setText(_translate("MainWindow", "Number of Episodes"))
        self.label_4.setText(_translate("MainWindow", "Mode"))
        self.createSeries.setText(_translate("MainWindow", "Create Series"))
        self.perEpisodeRb.setToolTip(_translate("MainWindow", "Creates sub directories for episodes inside a Season directory"))
        self.perEpisodeRb.setText(_translate("MainWindow", "Sub Directory Per Episode"))
        self.perSeasonRb.setToolTip(_translate("MainWindow", "Creates only Seasons directories and Subtitles directories inside them"))
        self.perSeasonRb.setText(_translate("MainWindow", "Directory Per Season Only"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tvShow), _translate("MainWindow", "TV Series"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
