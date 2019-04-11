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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folderPathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.folderPathLineEdit.setGeometry(QtCore.QRect(110, 20, 581, 22))
        self.folderPathLineEdit.setObjectName("folderPathLineEdit")
        self.openFolderPath = QtWidgets.QPushButton(self.centralwidget)
        self.openFolderPath.setGeometry(QtCore.QRect(10, 17, 93, 28))
        self.openFolderPath.setObjectName("openFolderPath")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 70, 671, 251))
        self.toolBox.setObjectName("toolBox")
        self.tvShow = QtWidgets.QWidget()
        self.tvShow.setGeometry(QtCore.QRect(0, 0, 671, 189))
        self.tvShow.setObjectName("tvShow")
        self.seriesName = QtWidgets.QLineEdit(self.tvShow)
        self.seriesName.setGeometry(QtCore.QRect(230, 30, 241, 22))
        self.seriesName.setObjectName("seriesName")
        self.label = QtWidgets.QLabel(self.tvShow)
        self.label.setGeometry(QtCore.QRect(140, 30, 81, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tvShow)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 121, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.numberOfSeasons = QtWidgets.QLineEdit(self.tvShow)
        self.numberOfSeasons.setGeometry(QtCore.QRect(230, 70, 241, 22))
        self.numberOfSeasons.setObjectName("numberOfSeasons")
        self.numberOfEpisodes = QtWidgets.QLineEdit(self.tvShow)
        self.numberOfEpisodes.setGeometry(QtCore.QRect(230, 110, 241, 22))
        self.numberOfEpisodes.setObjectName("numberOfEpisodes")
        self.label_3 = QtWidgets.QLabel(self.tvShow)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 121, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tvShow)
        self.label_4.setGeometry(QtCore.QRect(100, 150, 121, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.tvShow)
        self.comboBox.setGeometry(QtCore.QRect(230, 150, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.createSeries = QtWidgets.QPushButton(self.tvShow)
        self.createSeries.setGeometry(QtCore.QRect(530, 80, 93, 28))
        self.createSeries.setObjectName("createSeries")
        self.toolBox.addItem(self.tvShow, "")
        self.movies = QtWidgets.QWidget()
        self.movies.setGeometry(QtCore.QRect(0, 0, 671, 189))
        self.movies.setObjectName("movies")
        self.toolBox.addItem(self.movies, "")
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
        self.label.setText(_translate("MainWindow", "Series Name"))
        self.label_2.setText(_translate("MainWindow", "Number of Seasons"))
        self.label_3.setText(_translate("MainWindow", "Number of Episodes"))
        self.label_4.setText(_translate("MainWindow", "Mode"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Folder Per Episode"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Folder Per Season Only"))
        self.createSeries.setText(_translate("MainWindow", "Create Series"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tvShow), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.movies), _translate("MainWindow", "Page 2"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
