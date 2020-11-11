from PyQt5 import QtCore, QtGui, QtWidgets
from DecisionTree import Ui_DT
from KNeighbours import Ui_KNN
from RandomForest import Ui_RF
from SVM import Ui_SVM

class Ui_CHPT(object):
    def __init__(self):
        super().__init__()
        self.SVMValues = {}; self.DTValues = {}; self.KNNValues = {}; self.RTValues = {}
        self.SVMD = QtWidgets.QDialog();  self.SVMO = Ui_SVM();  self.SVMO.setupUi(self.SVMD)
        self.DTD = QtWidgets.QDialog();   self.DTO = Ui_DT();   self.DTO.setupUi(self.DTD)
        self.KNND = QtWidgets.QDialog();  self.KNNO = Ui_KNN();  self.KNNO.setupUi(self.KNND)
        self.RTD = QtWidgets.QDialog();   self.RTO = Ui_RF();    self.RTO.setupUi(self.RTD)
        self.SVMVal(); self.DTVal(); self.KNNVal(); self.RTVal()

        self.SVMO.Apply.clicked.connect(self.SVMVal)
        self.DTO.Apply.clicked.connect(self.DTVal)
        self.KNNO.Apply.clicked.connect(self.KNNVal)
        self.RTO.Apply.clicked.connect(self.RTVal)

    def setupUi(self, CHPT):
        CHPT.setObjectName("CHPT")
        CHPT.setFixedSize(500,200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CHPT.setWindowIcon(icon)
        CHPT.setStyleSheet("border-image: url(:/images/BackGround.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(CHPT)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SVM = QtWidgets.QCheckBox(CHPT)
        self.SVM.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SVM.setFont(font)
        self.SVM.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.SVM.setText("")
        self.SVM.setObjectName("SVM")
        self.horizontalLayout_3.addWidget(self.SVM)
        self.SVMLabel = QtWidgets.QLabel(CHPT)
        self.SVMLabel.setMinimumSize(QtCore.QSize(41, 29))
        self.SVMLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.SVMLabel.setObjectName("SVMLabel")
        self.horizontalLayout_3.addWidget(self.SVMLabel)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DT = QtWidgets.QCheckBox(CHPT)
        self.DT.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DT.setFont(font)
        self.DT.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.DT.setText("")
        self.DT.setObjectName("DT")
        self.horizontalLayout_2.addWidget(self.DT)
        self.DTLabel = QtWidgets.QLabel(CHPT)
        self.DTLabel.setMinimumSize(QtCore.QSize(111, 29))
        self.DTLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.DTLabel.setObjectName("DTLabel")
        self.horizontalLayout_2.addWidget(self.DTLabel)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.KNN = QtWidgets.QCheckBox(CHPT)
        self.KNN.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.KNN.setFont(font)
        self.KNN.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.KNN.setText("")
        self.KNN.setObjectName("KNN")
        self.horizontalLayout.addWidget(self.KNN)
        self.KNNLabel = QtWidgets.QLabel(CHPT)
        self.KNNLabel.setMinimumSize(QtCore.QSize(161, 29))
        self.KNNLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.KNNLabel.setObjectName("KNNLabel")
        self.horizontalLayout.addWidget(self.KNNLabel)
        self.horizontalLayout_13.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.RT = QtWidgets.QCheckBox(CHPT)
        self.RT.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RT.setFont(font)
        self.RT.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.RT.setText("")
        self.RT.setObjectName("RT")
        self.horizontalLayout_4.addWidget(self.RT)
        self.RTLabel = QtWidgets.QLabel(CHPT)
        self.RTLabel.setMinimumSize(QtCore.QSize(111, 29))
        self.RTLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.RTLabel.setObjectName("RTLabel")
        self.horizontalLayout_4.addWidget(self.RTLabel)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(18, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.NB = QtWidgets.QCheckBox(CHPT)
        self.NB.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NB.setFont(font)
        self.NB.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.NB.setText("")
        self.NB.setObjectName("NB")
        self.horizontalLayout_5.addWidget(self.NB)
        self.NBLabel = QtWidgets.QLabel(CHPT)
        self.NBLabel.setMinimumSize(QtCore.QSize(91, 29))
        self.NBLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.NBLabel.setObjectName("NBLabel")
        self.horizontalLayout_5.addWidget(self.NBLabel)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(158, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(28, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(168, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(168, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(168, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GNB = QtWidgets.QCheckBox(CHPT)
        self.GNB.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GNB.setFont(font)
        self.GNB.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.GNB.setText("")
        self.GNB.setObjectName("GNB")
        self.verticalLayout_2.addWidget(self.GNB)
        self.BNB = QtWidgets.QCheckBox(CHPT)
        self.BNB.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BNB.setFont(font)
        self.BNB.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.BNB.setText("")
        self.BNB.setObjectName("BNB")
        self.verticalLayout_2.addWidget(self.BNB)
        self.MNB = QtWidgets.QCheckBox(CHPT)
        self.MNB.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MNB.setFont(font)
        self.MNB.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.MNB.setText("")
        self.MNB.setObjectName("MNB")
        self.verticalLayout_2.addWidget(self.MNB)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.GNBLabel = QtWidgets.QLabel(CHPT)
        self.GNBLabel.setMinimumSize(QtCore.QSize(101, 29))
        self.GNBLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.GNBLabel.setObjectName("GNBLabel")
        self.verticalLayout.addWidget(self.GNBLabel)
        self.BNBLabel = QtWidgets.QLabel(CHPT)
        self.BNBLabel.setMinimumSize(QtCore.QSize(91, 29))
        self.BNBLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.BNBLabel.setObjectName("BNBLabel")
        self.verticalLayout.addWidget(self.BNBLabel)
        self.MNBLabel = QtWidgets.QLabel(CHPT)
        self.MNBLabel.setMinimumSize(QtCore.QSize(121, 29))
        self.MNBLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.MNBLabel.setObjectName("MNBLabel")
        self.verticalLayout.addWidget(self.MNBLabel)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(148, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(148, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(148, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(28, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem11, 4, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem12 = QtWidgets.QSpacerItem(298, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Restore = QtWidgets.QDialogButtonBox(CHPT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Restore.setFont(font)
        self.Restore.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Restore.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.Restore.setObjectName("Restore")
        self.horizontalLayout_11.addWidget(self.Restore)
        self.Cancel = QtWidgets.QDialogButtonBox(CHPT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_11.addWidget(self.Cancel)
        self.Apply = QtWidgets.QDialogButtonBox(CHPT)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.Apply.setFont(font)
        self.Apply.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Apply.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.Apply.setCenterButtons(False)
        self.Apply.setObjectName("Apply")
        self.horizontalLayout_11.addWidget(self.Apply)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout_15, 5, 0, 1, 1)

    
        self.GNB.setVisible(False)
        self.GNBLabel.setVisible(False)
        self.BNB.setVisible(False)
        self.BNBLabel.setVisible(False)
        self.MNB.setVisible(False)
        self.MNBLabel.setVisible(False)

        self.retranslateUi(CHPT)
        QtCore.QMetaObject.connectSlotsByName(CHPT)
        self.retranslateUi(CHPT)
        self.Cancel.accepted.connect(CHPT.accept)
        self.Cancel.rejected.connect(CHPT.reject)
        QtCore.QMetaObject.connectSlotsByName(CHPT)

        self.Restore.clicked.connect(self.reset)

        self.SVM.stateChanged.connect(self.SVMDailog)
        self.DT.stateChanged.connect(self.DTDailog)
        self.KNN.stateChanged.connect(self.KNNDailog)
        self.RT.stateChanged.connect(self.RTDailog)

    def SVMDailog(self):
        if self.SVM.isChecked():
            self.SVMD.show()
            self.SVMD.exec_()

    def DTDailog(self):
        if self.DT.isChecked():
            self.DTD.show()
            self.DTD.exec_()

    def KNNDailog(self):
        if self.KNN.isChecked():
            self.KNND.show()
            self.KNND.exec_()

    def RTDailog(self):
        if self.RT.isChecked():
            self.RTD.show()
            self.RTD.exec_()

 
    def SVMVal(self):
        kernel = self.SVMO.kernellist.currentText()
        gamma = self.SVMO.gammalist.currentText()
        dfs = self.SVMO.decision_function_shapelist.currentText()
        C = self.SVMO.CdoubleSpinBox.value()
        max_iter = self.SVMO.max_iterspinBox.value()
        degree = self.SVMO.degreespinBox.value()
        verbose = self.SVMO.verbosecheckBox.isChecked()
        probability = self.SVMO.probabilitycheckBox.isChecked()
        shrinking = self.SVMO.ShrinkingcheckBox.isChecked()

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
        # print(self.SVMValues)
        self.SVMD.accept()
    
    def DTVal(self):
        criterion = self.DTO.criterionlist.currentText()
        splitter = self.DTO.splitterlist.currentText()
        max_features = self.DTO.max_featureslist.currentText()
        min_samples_split = self.DTO.min_samples_splitdoubleSpinBox.value()
        max_depth = self.DTO.max_depthspinBox.value()
        min_samples_leaf = self.DTO.min_samples_leafspinBox.value()

        self.DTValues = {
            'criterion':[criterion],
            'splitter':[splitter],
            'max_features':[max_features],
            'min_samples_split':[min_samples_split],
            'max_depth':[max_depth],
            'min_samples_leaf':[min_samples_leaf]
        }
        # print(self.DTValues)
        self.DTD.accept()
    
    def KNNVal(self):
        algorithm = self.KNNO.algorithmlist.currentText()
        weights = self.KNNO.weightslist.currentText()
        p = self.KNNO.pspinBox.value()
        leaf_size = self.KNNO.leaf_sizespinBox.value()
        n_neighbors = self.KNNO.n_neighborsspinBox.value()

        self.KNNValues = {
            'algorithm':[algorithm],
            'weights':[weights],
            'p':[p],
            'leaf_size':[leaf_size],
            'n_neighbors':[n_neighbors]
        }
        # print(self.KNNValues)
        self.KNND.accept()
    
    def RTVal(self):
        criterion = self.RTO.criterionlist.currentText()
        max_features = self.RTO.max_featureslist.currentText()
        min_samples_split = self.RTO.min_samples_splitdoubleSpinBox.value()
        max_depth = self.RTO.max_depthspinBox.value()
        n_estimators = self.RTO.n_estimatorsspinBox.value()
        warm_start = self.RTO.warm_startcheckBox.isChecked()
        oob_score = self.RTO.oob_scorecheckBox.isChecked()
        bootstrap = self.RTO.bootstrapcheckBox.isChecked()

        self.RTValues = {
            'criterion':[criterion],
            'max_features':[max_features],
            'min_samples_split':[min_samples_split],
            'max_depth':[max_depth],
            'n_estimators':[n_estimators],
            'warm_start':[warm_start],
            'oob_score':[oob_score],
            'bootstrap':[bootstrap]
        }
        # print(self.RTValues)
        self.RTD.accept()
   
    def reset(self):
        self.SVM.setChecked(False)
        self.DT.setChecked(False)
        self.RT.setChecked(False)
        self.KNN.setChecked(False)
        self.NB.setChecked(False)
        self.GNB.setChecked(False)
        self.MNB.setChecked(False)
        self.BNB.setChecked(False)

    def retranslateUi(self, CHPT):
        _translate = QtCore.QCoreApplication.translate
        CHPT.setWindowTitle(_translate("CHPT", "Classification HyperParameter Tuning"))
        self.SVMLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">SVM</span></p></body></html>"))
        self.DTLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Decision Tree</span></p></body></html>"))
        self.KNNLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">KNearestNeighbors</span></p></body></html>"))
        self.RTLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Random Tree</span></p></body></html>"))
        self.NBLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">NaiveBayes</span></p></body></html>"))
        self.GNBLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">GaussianNB</span></p></body></html>"))
        self.BNBLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">BernouliNB</span></p></body></html>"))
        self.MNBLabel.setText(_translate("CHPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">MultinomialNB</span></p></body></html>"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    CHPT = QtWidgets.QDialog()
    ui = Ui_CHPT()
    ui.setupUi(CHPT)
    CHPT.show()
    sys.exit(app.exec_())
