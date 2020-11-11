from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
from LogisticRegression import Ui_LR

class Ui_HPT(object):
    def __init__(self):
        super().__init__()
        self.LValues = {}
        self.LRD = QtWidgets.QDialog()
        self.LR = Ui_LR()
        self.LR.setupUi(self.LRD)
        self.logisticValues()
        self.LR.Apply.clicked.connect(self.logisticValues)
        
    def setupUi(self, HPT):
        HPT.setObjectName("HPT")
        HPT.setFixedSize(400, 100)
        font = QtGui.QFont()
        font.setPointSize(10)
        HPT.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HPT.setWindowIcon(icon)
        HPT.setStyleSheet("border-image: url(:/images/BackGround.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(HPT)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LinearR = QtWidgets.QCheckBox(HPT)
        self.LinearR.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LinearR.setFont(font)
        self.LinearR.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.LinearR.setText("")
        self.LinearR.setObjectName("LinearR")
        self.horizontalLayout_2.addWidget(self.LinearR)
        self.LinearLabel = QtWidgets.QLabel(HPT)
        self.LinearLabel.setMinimumSize(QtCore.QSize(138, 29))
        self.LinearLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.LinearLabel.setObjectName("LinearLabel")
        self.horizontalLayout_2.addWidget(self.LinearLabel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LogisticR = QtWidgets.QCheckBox(HPT)
        self.LogisticR.setMinimumSize(QtCore.QSize(24, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LogisticR.setFont(font)
        self.LogisticR.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.LogisticR.setText("")
        self.LogisticR.setObjectName("LogisticR")
        self.horizontalLayout_3.addWidget(self.LogisticR)
        self.LogisticLabel = QtWidgets.QLabel(HPT)
        self.LogisticLabel.setMinimumSize(QtCore.QSize(151, 29))
        self.LogisticLabel.setStyleSheet("border-image: url(:/images/1WhiteTransparent.png);")
        self.LogisticLabel.setObjectName("LogisticLabel")
        self.horizontalLayout_3.addWidget(self.LogisticLabel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Restore = QtWidgets.QDialogButtonBox(HPT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Restore.setFont(font)
        self.Restore.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Restore.setStandardButtons(QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.Restore.setObjectName("Restore")
        self.horizontalLayout.addWidget(self.Restore)
        self.Cancel = QtWidgets.QDialogButtonBox(HPT)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.Apply = QtWidgets.QDialogButtonBox(HPT)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.Apply.setFont(font)
        self.Apply.setStyleSheet("border-image: url(:/images/1WhiteBackground.jpg);")
        self.Apply.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.Apply.setCenterButtons(False)
        self.Apply.setObjectName("Apply")
        self.horizontalLayout.addWidget(self.Apply)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(HPT)
        QtCore.QMetaObject.connectSlotsByName(HPT)
        self.retranslateUi(HPT)
        self.Cancel.accepted.connect(HPT.accept)
        self.Cancel.rejected.connect(HPT.reject)
        QtCore.QMetaObject.connectSlotsByName(HPT)
        
        self.Restore.clicked.connect(self.reset)
        self.LogisticR.stateChanged.connect(self.logistic)

    def logistic(self):
        if self.LogisticR.isChecked():
            self.LRD.show()
            self.LRD.exec_()

    def logisticValues(self):
        penalty = self.LR.penaltylist.currentText()
        solver = self.LR.solverlist.currentText()
        multi_class = self.LR.multiclasslist.currentText()
        C = self.LR.CdoubleSpinBox.value()
        max_iter = self.LR.max_tierspinBox.value()
        n_jobs = self.LR.n_jobsspinBox.value()
        dual = self.LR.dualcheckBox.isChecked()
        warm_start = self.LR.warmstartcheckBox.isChecked()
        fit_intercept = self.LR.fitinterceptcheckBox.isChecked()

        self.LValues = {
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
        # print(self.LValues)
        self.LRD.accept()

    def reset(self):
        self.LinearR.setChecked(False)
        self.LogisticR.setChecked(False)

    def retranslateUi(self, HPT):
        _translate = QtCore.QCoreApplication.translate
        HPT.setWindowTitle(_translate("HPT", "Regression HyperParameter Tuning"))
        self.LinearLabel.setText(_translate("HPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Linear Regression</span></p></body></html>"))
        self.LogisticLabel.setText(_translate("HPT", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Logistic Regression</span></p></body></html>"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    HPT = QtWidgets.QDialog()
    ui = Ui_HPT()
    ui.setupUi(HPT)
    HPT.show()
    sys.exit(app.exec_())
