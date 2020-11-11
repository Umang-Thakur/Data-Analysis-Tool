import pickle
from PyQt5.QtGui import QIcon
from sklearn import exceptions as skex
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import GridSearchCV

from sklearn import datasets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from DecisionTree import Ui_DT
from KNeighbours import Ui_KNN
from RandomForest import Ui_RF
from SVM import Ui_SVM
from LogisticRegression import Ui_LR
from CHPT import Ui_CHPT
from HPT import Ui_HPT
from Target import Ui_Target

import pandas as pd
import time

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.x = []
        self.y = []
        self.model = None; self.output = []
        self.df = pd.DataFrame()
        self.col = ""

        self.path = ""
        self.SVMValues = {}; self.DTValues = {}; self.KNNValues = {}; self.RTValues = {}; self.LRValues = {};
        self.CHPTDM = QtWidgets.QDialog();  self.CHPTOM = Ui_CHPT();  self.CHPTOM.setupUi(self.CHPTDM)
        self.HPTDM = QtWidgets.QDialog();   self.HPTOM = Ui_HPT();    self.HPTOM.setupUi(self.HPTDM)
        self.SVMDM = QtWidgets.QDialog();   self.SVMOM = Ui_SVM();    self.SVMOM.setupUi(self.SVMDM)
        self.DTDM = QtWidgets.QDialog();    self.DTOM = Ui_DT();      self.DTOM.setupUi(self.DTDM)
        self.KNNDM = QtWidgets.QDialog();   self.KNNOM = Ui_KNN();    self.KNNOM.setupUi(self.KNNDM)
        self.RTDM = QtWidgets.QDialog();    self.RTOM = Ui_RF();      self.RTOM.setupUi(self.RTDM)
        self.LRDM = QtWidgets.QDialog();    self.LRM = Ui_LR();       self.LRM.setupUi(self.LRDM)
        self.TRDM = QtWidgets.QDialog();    self.TRM = Ui_Target();   self.TRM.setupUi(self.TRDM)
        self.CHPTOM.NB.stateChanged.connect(self.NaivesBayes)
        self.SVMVal(); self.LRVal(); self.DTVal(); self.KNNVal(); self.RTVal()
        self.CHPTValues = {
            'SVM': self.SVMValues,
            'DecisionTree': self.DTValues,
            'KNearestNeighbours':self.KNNValues,
            'RandomForest':self.RTValues
        }
        self.HPTValues = { 'Logistic Regression':self.LRValues }
        
        self.SVMOM.Apply.clicked.connect(self.SVMVal)
        self.DTOM.Apply.clicked.connect(self.DTVal)
        self.KNNOM.Apply.clicked.connect(self.KNNVal)
        self.RTOM.Apply.clicked.connect(self.RTVal)
        self.LRM.Apply.clicked.connect(self.LRVal)
        self.CHPTOM.Apply.clicked.connect(self.CHPTVal)
        self.HPTOM.Apply.clicked.connect(self.HPTVal)
      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(843, 665)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("border-image: url(:/images/MainBackGround.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setMinimumSize(QtCore.QSize(771, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Logo.setFont(font)
        self.Logo.setStyleSheet("border-image: url(:/images/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.verticalLayout.addWidget(self.Logo)
        self.msg1 = QtWidgets.QLabel(self.centralwidget)
        self.msg1.setMinimumSize(QtCore.QSize(181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.msg1.setFont(font)
        self.msg1.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.msg1.setScaledContents(True)
        self.msg1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msg1.setObjectName("msg1")
        self.verticalLayout.addWidget(self.msg1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(138, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.FilePath = QtWidgets.QLabel(self.centralwidget)
        self.FilePath.setMinimumSize(QtCore.QSize(497, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FilePath.setFont(font)
        self.FilePath.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);\n"
"border-radius: 6;")
        self.FilePath.setText("")
        self.FilePath.setScaledContents(True)
        self.FilePath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FilePath.setObjectName("FilePath")
        self.horizontalLayout.addWidget(self.FilePath)
        spacerItem1 = QtWidgets.QSpacerItem(168, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(798, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(78, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.DisplayData = QtWidgets.QPushButton(self.centralwidget)
        self.DisplayData.setMinimumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DisplayData.setFont(font)
        self.DisplayData.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);\n"
"border-radius: 6;")
        self.DisplayData.setObjectName("DisplayData")
        self.horizontalLayout_2.addWidget(self.DisplayData)
        spacerItem4 = QtWidgets.QSpacerItem(18, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.EditData = QtWidgets.QComboBox(self.centralwidget)
        self.EditData.setMinimumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EditData.setFont(font)
        self.EditData.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EditData.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.EditData.setObjectName("EditData")
        self.EditData.addItem("")
        self.EditData.addItem("")
        self.EditData.addItem("")
        self.horizontalLayout_2.addWidget(self.EditData)
        spacerItem5 = QtWidgets.QSpacerItem(18, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.DescribeDate = QtWidgets.QPushButton(self.centralwidget)
        self.DescribeDate.setMinimumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DescribeDate.setFont(font)
        self.DescribeDate.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);\n"
"border-radius: 6;")
        self.DescribeDate.setObjectName("DescribeDate")
        self.horizontalLayout_2.addWidget(self.DescribeDate)
        spacerItem6 = QtWidgets.QSpacerItem(118, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(798, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(158, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.FeatureTuning = QtWidgets.QPushButton(self.centralwidget)
        self.FeatureTuning.setMinimumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FeatureTuning.setFont(font)
        self.FeatureTuning.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);\n"
"border-radius: 6;")
        self.FeatureTuning.setObjectName("FeatureTuning")
        self.horizontalLayout_4.addWidget(self.FeatureTuning)
        spacerItem9 = QtWidgets.QSpacerItem(18, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.DropBox = QtWidgets.QComboBox(self.centralwidget)
        self.DropBox.setMinimumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DropBox.setFont(font)
        self.DropBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DropBox.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.DropBox.setObjectName("DropBox")
        self.DropBox.addItem("")
        self.DropBox.addItem("")
        self.DropBox.addItem("")
        self.horizontalLayout_4.addWidget(self.DropBox)
        spacerItem10 = QtWidgets.QSpacerItem(238, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(795, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem11)
        self.msg2 = QtWidgets.QLabel(self.centralwidget)
        self.msg2.setMinimumSize(QtCore.QSize(191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.msg2.setFont(font)
        self.msg2.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.msg2.setScaledContents(True)
        self.msg2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msg2.setObjectName("msg2")
        self.verticalLayout.addWidget(self.msg2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(28, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.ModelType = QtWidgets.QComboBox(self.centralwidget)
        self.ModelType.setMinimumSize(QtCore.QSize(181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ModelType.setFont(font)
        self.ModelType.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.ModelType.setObjectName("ModelType")
        self.ModelType.addItem("")
        self.ModelType.addItem("")
        self.ModelType.addItem("")
        self.horizontalLayout_6.addWidget(self.ModelType)
        self.RegressionType = QtWidgets.QComboBox(self.centralwidget)
        self.RegressionType.setEnabled(True)
        self.RegressionType.setMinimumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RegressionType.setFont(font)
        self.RegressionType.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.RegressionType.setObjectName("RegressionType")
        self.RegressionType.addItem("")
        self.RegressionType.addItem("")
        self.RegressionType.addItem("")
        self.RegressionType.addItem("")
        self.horizontalLayout_6.addWidget(self.RegressionType)
        self.ClassificationType = QtWidgets.QComboBox(self.centralwidget)
        self.ClassificationType.setMinimumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ClassificationType.setFont(font)
        self.ClassificationType.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.ClassificationType.setObjectName("ClassificationType")
        self.ClassificationType.addItem("")
        self.ClassificationType.addItem("")
        self.ClassificationType.addItem("")
        self.ClassificationType.addItem("")
        self.ClassificationType.addItem("")
        self.ClassificationType.addItem("")
        self.ClassificationType.addItem("")
        self.horizontalLayout_6.addWidget(self.ClassificationType)
        self.ClassificationTypeNB = QtWidgets.QComboBox(self.centralwidget)
        self.ClassificationTypeNB.setMinimumSize(QtCore.QSize(141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ClassificationTypeNB.setFont(font)
        self.ClassificationTypeNB.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.ClassificationTypeNB.setObjectName("ClassificationTypeNB")
        self.ClassificationTypeNB.addItem("")
        self.ClassificationTypeNB.addItem("")
        self.ClassificationTypeNB.addItem("")
        self.horizontalLayout_6.addWidget(self.ClassificationTypeNB)
        spacerItem13 = QtWidgets.QSpacerItem(28, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem14 = QtWidgets.QSpacerItem(808, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(729, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.Train = QtWidgets.QPushButton(self.centralwidget)
        self.Train.setMinimumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Train.setFont(font)
        self.Train.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);\n"
"border-radius: 6;")
        self.Train.setObjectName("Train")
        self.horizontalLayout_3.addWidget(self.Train)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(818, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem15)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 843, 26))
        self.menuBar.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionData_Cleaning = QtWidgets.QAction(MainWindow)
        self.actionData_Cleaning.setObjectName("actionData_Cleaning")
        self.actionModel_Training = QtWidgets.QAction(MainWindow)
        self.actionModel_Training.setObjectName("actionModel_Training")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionAbout_Model_Traning = QtWidgets.QAction(MainWindow)
        self.actionAbout_Model_Traning.setObjectName("actionAbout_Model_Traning")
        self.actionAs_CSV = QtWidgets.QAction(MainWindow)
        self.actionAs_CSV.setObjectName("actionAs_CSV")
        self.actionAs_PDF = QtWidgets.QAction(MainWindow)
        self.actionAs_PDF.setObjectName("actionAs_PDF")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuSave.addAction(self.actionAs_CSV)
        self.menuSave.addSeparator()
        self.menuSave.addAction(self.actionAs_PDF)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPredict)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Model_Traning)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
              
        self.RegressionType.setHidden(True)
        self.ClassificationType.setHidden(True)
        self.ClassificationTypeNB.setHidden(True)

        self.ModelType.currentIndexChanged.connect(self.mtype)
        self.ClassificationType.currentIndexChanged.connect(self.ctype)
        self.RegressionType.currentIndexChanged.connect(self.Regression)

        self.Train.clicked.connect(self.ModelTrain)
        self.actionPredict.triggered.connect(self.predict)
        self.actionExit.triggered.connect(self.Quit)
        self.RegressionType.currentIndexChanged.connect(self.TrainModelR)
        self.ClassificationTypeNB.currentIndexChanged.connect(self.ntype)
        self.actionAs_CSV.setText("Save Cleaned Data")
        self.actionAs_PDF.setText("Save Predicted Data")
        self.actionAs_CSV.triggered.connect(self.SaveCD)
        self.actionAs_PDF.triggered.connect(self.SavePD)
        self.actionSave.triggered.connect(self.SaveDF)


    ''' ComboBoxes '''
    def NaivesBayes(self):
        self.progressBar.setValue(0)
        self.model = None
        if(self.CHPTOM.NB.isChecked()):
            self.CHPTOM.GNB.setVisible(True); self.CHPTOM.GNBLabel.setVisible(True)
            self.CHPTOM.BNB.setVisible(True); self.CHPTOM.BNBLabel.setVisible(True)
            self.CHPTOM.MNB.setVisible(True); self.CHPTOM.MNBLabel.setVisible(True)
            self.CHPTDM.setFixedHeight(260)
        else:
            self.CHPTOM.GNB.setVisible(False); self.CHPTOM.GNBLabel.setVisible(False); self.CHPTOM.GNB.setChecked(False)
            self.CHPTOM.BNB.setVisible(False); self.CHPTOM.BNBLabel.setVisible(False); self.CHPTOM.BNB.setChecked(False)
            self.CHPTOM.MNB.setVisible(False); self.CHPTOM.MNBLabel.setVisible(False); self.CHPTOM.MNB.setChecked(False)
            self.CHPTDM.setFixedHeight(200)
            self.model = None

    def ntype(self):
        self.progressBar.setValue(0)
        self.model = None
        if self.ClassificationTypeNB.currentIndex() == 0:
            self.model = GaussianNB()
        elif self.ClassificationTypeNB.currentIndex() == 1:
            self.model = BernoulliNB()
        elif self.ClassificationTypeNB.currentIndex() == 2:
            self.model = MultinomialNB()
        else:
            self.model = None
            
    def ctype(self):
        self.progressBar.setValue(0)
        self.model = None
        if self.ClassificationType.currentIndex() == 0:    
            self.model = None
            self.ClassificationTypeNB.setCurrentIndex(0); self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
        elif self.ClassificationType.currentIndex() == 1:
            self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
            self.SVMDM.show()
            if (self.SVMDM.exec_()):  
                self.model = GridSearchCV(SVC(), self.SVMValues, cv=2, return_train_score=False)
            else:
                self.model = None
                self.SVMDM.close()
        elif self.ClassificationType.currentIndex() == 2:
            self.ClassificationTypeNB.setVisible(True); self.RegressionType.setHidden(True)
        elif self.ClassificationType.currentIndex() == 3:
            self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
            self.DTDM.show()
            if(self.DTDM.exec_()):
                self.model = GridSearchCV(DecisionTreeClassifier(), self.DTValues, cv=2, return_train_score=False)
            else:
                self.model = None
                self.DTDM.close()
        elif self.ClassificationType.currentIndex() == 4:
            self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
            self.RTDM.show()
            if(self.RTDM.exec_()):
                self.model = GridSearchCV(RandomForestClassifier(), self.RTValues, cv=2, return_train_score=False)
            else:
                self.model = None
                self.RTDM.close()
        elif self.ClassificationType.currentIndex() == 5:
            self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
            self.KNNDM.show()
            if(self.KNNDM.exec_()):
                self.model = GridSearchCV(KNeighborsClassifier(), self.KNNValues, cv=2, return_train_score=False)
            else:
                self.model = None
                self.KNNDM.close()
        elif self.ClassificationType.currentIndex() == 6:
            bestscore = {}
            self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
            self.CHPTDM.show()
            if(self.CHPTDM.exec_()):
                if self.CHPTOM.SVM.isChecked():
                    self.model = GridSearchCV(SVC(), self.CHPTOM.SVMValues, cv=2, return_train_score=False)
                    self.model.fit(self.x, self.y)
                    bestscore[round(self.model.score(self.x, self.y)*100)] = 1
                if self.CHPTOM.DT.isChecked():
                    self.model = GridSearchCV(DecisionTreeClassifier(), self.CHPTOM.DTValues, cv=2, return_train_score=False)
                    self.model.fit(self.x, self.y)
                    bestscore[round(self.model.score(self.x, self.y)*100)] = 2
                if self.CHPTOM.RT.isChecked():
                    self.model = GridSearchCV(RandomForestClassifier(), self.CHPTOM.RTValues, cv=2, return_train_score=False)
                    self.model.fit(self.x, self.y)
                    bestscore[round(self.model.score(self.x, self.y)*100)] = 4
                if self.CHPTOM.KNN.isChecked():
                    self.model = GridSearchCV(KNeighborsClassifier(), self.CHPTOM.KNNValues, cv=2, return_train_score=False)
                    self.model.fit(self.x, self.y)
                    bestscore[round(self.model.score(self.x, self.y)*100)] = 3
                if self.CHPTOM.NB.isChecked():
                    if self.CHPTOM.BNB.isChecked():
                        self.model = BernoulliNB()
                        self.model.fit(self.x, self.y)
                        bestscore[round(self.model.score(self.x, self.y)*100)] = 6
                    if self.CHPTOM.MNB.isChecked():
                        self.model = MultinomialNB()
                        self.model.fit(self.x, self.y)
                        bestscore[round(self.model.score(self.x, self.y)*100)] = 7
                    if self.CHPTOM.GNB.isChecked():
                        self.model = GaussianNB()
                        self.model.fit(self.x, self.y)
                        bestscore[round(self.model.score(self.x, self.y)*100)] = 5
                try:
                    self.maxscore = max(bestscore.keys())
                    model_list = [0,
                            GridSearchCV(SVC(), self.CHPTOM.SVMValues, cv=2, return_train_score=False),
                            GridSearchCV(DecisionTreeClassifier(), self.CHPTOM.DTValues, cv=2, return_train_score=False),
                            GridSearchCV(KNeighborsClassifier(), self.CHPTOM.KNNValues, cv=2, return_train_score=False),
                            GridSearchCV(RandomForestClassifier(), self.CHPTOM.RTValues, cv=2, return_train_score=False),
                            GaussianNB(), BernoulliNB(), MultinomialNB()
                            ]
                    self.model = model_list[bestscore[self.maxscore]]
                except ValueError:
                    self.model = None
            else:
                self.model = None
                self.CHPTDM.close()

    def mtype(self):
        self.progressBar.setValue(0)
        self.model = None
        if self.ModelType.currentIndex() == 0:
            self.model = None
            self.RegressionType.setCurrentIndex(0); self.ClassificationType.setCurrentIndex(0); self.ClassificationTypeNB.setCurrentIndex(0)
            self.RegressionType.setHidden(True); self.ClassificationType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
        elif self.ModelType.currentIndex() == 1:
            self.model = None
            self.ClassificationType.setCurrentIndex(0); self.ClassificationTypeNB.setCurrentIndex(0)
            self.RegressionType.setVisible(True); self.ClassificationType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
        elif self.ModelType.currentIndex() == 2:
            self.model = None
            self.RegressionType.setCurrentIndex(0); self.ClassificationTypeNB.setCurrentIndex(0)
            self.ClassificationType.setVisible(True); self.RegressionType.setHidden(True); self.ClassificationTypeNB.setHidden(True)
        
    def Regression(self):
        self.progressBar.setValue(0)
        self.model = None
        if self.RegressionType.currentIndex() == 0:
            self.model = None
        elif self.RegressionType.currentIndex() == 1:
            self.model = LinearRegression()
        elif self.RegressionType.currentIndex() == 2:
            self.LRDM.show()
            if (self.LRDM.exec_()):
                self.model = GridSearchCV(LogisticRegression(), self.LRValues, cv=2 ,return_train_score=False)
            else:
                self.model = None
                self.LRDM.close()
        elif self.RegressionType.currentIndex() == 3:
            self.HPTDM.show()
            if (not self.HPTDM.exec_()):
                self.model = None
                self.HPTDM.close()


    ''' Model training & Prediction'''
    def TrainModelR(self):
        self.model = None
        if self.RegressionType.currentIndex() == 1:
            self.model = LinearRegression()
        elif self.RegressionType.currentIndex() == 2:
            self.model = GridSearchCV(LogisticRegression(), self.LRValues, cv=2 ,return_train_score=False)
        elif self.RegressionType.currentIndex() == 3:
            try:
                if self.HPTValues['Linear Regression'] == True and self.HPTValues['LogisticR'] == True:
                    self.Li = LinearRegression()
                    self.Li.fit(self.x, self.y)
                    LIScore = round(self.Li.score(self.x, self.y) * 100)
                    self.Lo = GridSearchCV(LogisticRegression(), self.HPTValues['Logistic Regression'], cv=5 ,return_train_score=False)
                    self.Lo.fit(self.x , self.y)
                    LOScore = round(self.Lo.best_score_ * 100)
                    if LOScore > LIScore:
                        self.model = self.Lo
                    else:
                        self.model = self.Li
                elif self.HPTValues['Linear Regression'] == True:
                    self.model = LinearRegression() 
                elif self.HPTValues['LogisticR'] == True:
                    self.model = GridSearchCV(LogisticRegression(), self.LRValues, cv=2 ,return_train_score=False)
                else:
                    self.model = None
                    self.HPTDM.close()
            except KeyError:
                print()

    def TrainModel(self):
        self.ModelTrain()

    def LOADDataFrame(self):
        pickle_in = open("DataFrame\\DataFrame.pickle","rb")
        data = pickle.load(pickle_in)
        self.TRDM.show()
        self.TRM.TargetBox.addItems(data.columns.tolist())
        if self.TRDM.exec_() == 1:
            try:
                temp_df = data.copy()
                self.x = temp_df.drop(self.TRM.TargetBox.currentText(), 1)
                self.y = temp_df[self.TRM.TargetBox.currentText()]
                self.col = self.TRM.TargetBox.currentText()
                self.x, self.xt, self.y, self.yt = train_test_split(self.x, self.y, test_size = 0.2)
                self.TRDM.accept()
            except ValueError:
                self.TRDM.close()

    def ModelTrain(self):
        if not (self.model == None):
            self.LOADDataFrame()
            self.model.fit(self.x , self.y)
            for i in range(0,101,1):
                self.progressBar.setValue(i)
                time.sleep(0.1)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Cannot Train Model")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("You didn't select any model to train on.")
            msg.setWindowIcon(QtGui.QIcon('Images/Warning.png'))
            msg.exec_()
    
    def predict(self):
        if(self.model == None):
            self.output = []
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Cannot Predict")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("You didn't train any model to predict on.")
            msg.setWindowIcon(QtGui.QIcon('Images/Warning.png'))
            msg.exec_()
        else:
            try:
                self.output = self.model.predict(self.x)
            except skex.NotFittedError:
                print()


    ''' MenuButton Functions '''
    def Quit(self):
        exit()

    def SaveCD(self):
        print()
    
    def SavePD(self):
        if not (len(self.output) == 0):
            self.df[self.col] = self.output
            filename = QFileDialog.getSaveFileName()
            if not (len(filename[0]) == 0):
                self.path = filename[0]
                self.df.to_csv(self.path + '.csv', index=False)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Cannot Save Predicted File")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("You didn't predict the values.")
            msg.setWindowIcon(QtGui.QIcon('Images/Warning.png'))
            msg.exec_()


    ''' Taking Values from dialog box '''
    def LRVal(self):
        penalty = self.LRM.penaltylist.currentText()
        solver = self.LRM.solverlist.currentText()
        multi_class = self.LRM.multiclasslist.currentText()
        C = self.LRM.CdoubleSpinBox.value()
        max_iter = self.LRM.max_tierspinBox.value()
        n_jobs = self.LRM.n_jobsspinBox.value()
        dual = self.LRM.dualcheckBox.isChecked()
        warm_start = self.LRM.warmstartcheckBox.isChecked()
        fit_intercept = self.LRM.fitinterceptcheckBox.isChecked()

        self.LRValues = {
            'penalty':[penalty],
            'solver':[solver],
            'multi_class':[multi_class],
            'C':[C],
            'max_iter':[max_iter],
            'n_jobs':[n_jobs],
            'dual':[dual],
            'warm_start':[warm_start],
            'fit_intercept':[fit_intercept]
        }
        self.LRDM.accept()
 
    def SVMVal(self):
        kernel = self.SVMOM.kernellist.currentText()
        gamma = self.SVMOM.gammalist.currentText()
        dfs = self.SVMOM.decision_function_shapelist.currentText()
        C = self.SVMOM.CdoubleSpinBox.value()
        max_iter = self.SVMOM.max_iterspinBox.value()
        degree = self.SVMOM.degreespinBox.value()
        verbose = self.SVMOM.verbosecheckBox.isChecked()
        probability = self.SVMOM.probabilitycheckBox.isChecked()
        shrinking = self.SVMOM.ShrinkingcheckBox.isChecked()

        self.SVMValues = {
            'kernel':[kernel],
            'gamma':[gamma],
            'decision_function_shape':[dfs],
            'C':[C],
            'max_iter':[max_iter],
            'degree':[degree],
            'verbose':[verbose],
            'probability':[probability],
            'shrinking':[shrinking]
        }
        self.SVMDM.accept()
    
    def DTVal(self):
        criterion = self.DTOM.criterionlist.currentText()
        splitter = self.DTOM.splitterlist.currentText()
        max_features = self.DTOM.max_featureslist.currentText()
        min_samples_split = self.DTOM.min_samples_splitdoubleSpinBox.value()
        max_depth = self.DTOM.max_depthspinBox.value()
        min_samples_leaf = self.DTOM.min_samples_leafspinBox.value()

        self.DTValues = {
            'criterion':[criterion],
            'splitter':[splitter],
            'max_features':[max_features],
            'min_samples_split':[min_samples_split],
            'max_depth':[max_depth],
            'min_samples_leaf':[min_samples_leaf]
        }
        self.DTDM.accept()
    
    def KNNVal(self):
        algorithm = self.KNNOM.algorithmlist.currentText()
        weights = self.KNNOM.weightslist.currentText()
        p = self.KNNOM.pspinBox.value()
        leaf_size = self.KNNOM.leaf_sizespinBox.value()
        n_neighbors = self.KNNOM.n_neighborsspinBox.value()

        self.KNNValues = {
            'algorithm':[algorithm],
            'weights':[weights],
            'p':[p],
            'leaf_size':[leaf_size],
            'n_neighbors':[n_neighbors]
        }
        self.KNNDM.accept()
    
    def RTVal(self):
        criterion = self.RTOM.criterionlist.currentText()
        max_features = self.RTOM.max_featureslist.currentText()
        min_samples_split = self.RTOM.min_samples_splitdoubleSpinBox.value()
        max_depth = self.RTOM.max_depthspinBox.value()
        n_estimators = self.RTOM.n_estimatorsspinBox.value()
        warm_start = self.RTOM.warm_startcheckBox.isChecked()
        oob_score = self.RTOM.oob_scorecheckBox.isChecked()
        bootstrap = self.RTOM.bootstrapcheckBox.isChecked()

        self.RTValues = {
            'criterion':[criterion],
            'max_features':[max_features],
            'min_samples_split':[min_samples_split],
            'max_depth':[max_depth],
            'n_estimators':[n_estimators],
            'warm_start':[warm_start],
            'oob_score':[oob_score],
            'bootstrap':[bootstrap]}
        self.RTDM.accept()

    def CHPTVal(self):
        self.CHPTValues['SVM'] = self.CHPTOM.SVMValues
        self.CHPTValues['DecisionTree'] = self.CHPTOM.DTValues
        self.CHPTValues['KNearestNeighbours'] = self.CHPTOM.KNNValues
        self.CHPTValues['RandomForest'] = self.CHPTOM.RTValues
        self.CHPTDM.accept()

    def HPTVal(self):
        if self.HPTOM.LinearR.isChecked():
            self.HPTValues['Linear Regression'] = True
        else:
            self.HPTValues['Linear Regression'] = False 
        if self.HPTOM.LogisticR.isChecked():
            self.HPTValues['LogisticR'] = True
        else:
            self.HPTValues['LogisticR'] = False    
        self.HPTValues['Logistic Regression'] = self.HPTOM.LValues
        self.HPTDM.accept()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Analysis"))
        self.msg1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">DATA CLEANING</span></p></body></html>"))
        self.DisplayData.setText(_translate("MainWindow", "Display Data"))
        self.EditData.setItemText(0, _translate("MainWindow", "Modification"))
        self.EditData.setItemText(1, _translate("MainWindow", "Delete Rows"))
        self.EditData.setItemText(2, _translate("MainWindow", "One Hot Encode"))
        self.DescribeDate.setText(_translate("MainWindow", "Describe Data"))
        self.FeatureTuning.setText(_translate("MainWindow", "Feature Tuning"))
        self.DropBox.setItemText(0, _translate("MainWindow", "Graphical View"))
        self.DropBox.setItemText(1, _translate("MainWindow", "Histogram"))
        self.DropBox.setItemText(2, _translate("MainWindow", "Correlation Data"))
        self.msg2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">MODEL TRAINING</span></p></body></html>"))
        self.ModelType.setItemText(0, _translate("MainWindow", "Select Problem Type"))
        self.ModelType.setItemText(1, _translate("MainWindow", "Regression"))
        self.ModelType.setItemText(2, _translate("MainWindow", "Classification"))
        self.RegressionType.setItemText(0, _translate("MainWindow", "Regression Type"))
        self.RegressionType.setItemText(1, _translate("MainWindow", "Linear Regression"))
        self.RegressionType.setItemText(2, _translate("MainWindow", "Logistic Regression"))
        self.RegressionType.setItemText(3, _translate("MainWindow", "Hyper Parmeter Tuning"))
        self.ClassificationType.setItemText(0, _translate("MainWindow", "Classification Type"))
        self.ClassificationType.setItemText(1, _translate("MainWindow", "SVM"))
        self.ClassificationType.setItemText(2, _translate("MainWindow", "NaiveBayes"))
        self.ClassificationType.setItemText(3, _translate("MainWindow", "DecisionTree"))
        self.ClassificationType.setItemText(4, _translate("MainWindow", "RandomForest"))
        self.ClassificationType.setItemText(5, _translate("MainWindow", "KNearestNeighbors"))
        self.ClassificationType.setItemText(6, _translate("MainWindow", "Hyper Parmeter Tuning"))
        self.ClassificationTypeNB.setItemText(0, _translate("MainWindow", "GaussianNB"))
        self.ClassificationTypeNB.setItemText(1, _translate("MainWindow", "BernoulliNB"))
        self.ClassificationTypeNB.setItemText(2, _translate("MainWindow", "MultinomialNB"))
        self.Train.setText(_translate("MainWindow", "Train"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Output"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionData_Cleaning.setText(_translate("MainWindow", "Data Cleaning"))
        self.actionModel_Training.setText(_translate("MainWindow", "Model Training"))
        self.actionVersion.setText(_translate("MainWindow", "ClearAll"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open File"))
        self.actionAbout_2.setText(_translate("MainWindow", "About Data Cleaning"))
        self.actionAbout_Model_Traning.setText(_translate("MainWindow", "About Model Traning"))
        self.actionAs_CSV.setText(_translate("MainWindow", "as CSV"))
        self.actionAs_PDF.setText(_translate("MainWindow", "as PDF"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
