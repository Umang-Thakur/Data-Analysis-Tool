from typing import Iterable
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, pickle
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QComboBox
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import seaborn
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

from df_table import pandasModel
from Read_dialog import Ui_Dialog
from MainWindow import Ui_MainWindow
from table import Ui_Table
from Edit_data import Ui_edit_data
from Describe_data import Ui_desc_data
from Histogram import Ui_Hist
from Feature import Ui_Feature_Tune

f_path = str()
cols = None
df = pd.DataFrame()

class Table(QtWidgets.QDialog, Ui_Table):
    def __init__(self, df, parent =  None):
        super(Table, self).__init__(parent)
        self.setupUi(self)
        self.tableView.setModel(df)

class EditData(QtWidgets.QDialog, Ui_edit_data):
    def __init__(self, cols = Iterable[str], sel = str,parent =  None):
        super(EditData, self).__init__(parent)
        self.setupUi(self)
        self.comboBox.currentTextChanged.connect(self.opt_1)
        self.comboBox_2.currentTextChanged.connect(self.opt_2)
        self.comboBox.addItems(cols)
        self.buttonBox.accepted.connect(self.edit)
        self.opt = []
        self.sel = sel

    def opt_1(self):
        if self.comboBox.currentText() != 'SELECT':
            if self.sel == 'Delete Rows':
                self.label_2.setVisible(True)
                self.comboBox_2.setVisible(True)
            else:
                self.label_2.setVisible(False)
                self.comboBox_2.setVisible(False)

    def opt_2(self):
        if self.comboBox_2.currentText() == 'On Condition':
            self.label_3.setVisible(True)
            self.lineEdit.setVisible(True)
            self.comboBox_3.setVisible(True)
            self.label_4.setVisible(True)
        else:
            self.comboBox_3.setVisible(False)
            self.label_3.setVisible(False)
            self.lineEdit.setVisible(False)
            self.label_4.setVisible(False)

    def edit(self):
        option_1 = self.comboBox.currentText()
        option_2 = self.comboBox_2.currentText()
        option_3 = self.lineEdit.text()
        option_4 = self.comboBox_3.currentIndex()
        self.opt.append(option_1)
        self.opt.append(option_2)
        self.opt.append(option_3)
        self.opt.append(option_4)
        self.accept()

class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, cols = Iterable[str],parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.options = []
        # Connecting click events
        self.comboBox.currentTextChanged.connect(self.check_opt)
        self.comboBox_2.setVisible(False)
        self.label_2.setVisible(False)

        # Setting up Cols parameter
        self.comboBox_2.addItems(cols)

    def read_data(self):
       option_1 =  self.comboBox.currentText()
       option_2 = self.comboBox_2.currentText()
       self.options.append(option_1)
       self.options.append(option_2)
       self.accept()
    
    def check_opt(self, value):
        if value == 'Column Data':
            self.comboBox_2.setVisible(True)
            self.label_2.setVisible(True)
        else:
            self.comboBox_2.setVisible(False)
            self.label_2.setVisible(False)

class Desc_data(QtWidgets.QDialog, Ui_desc_data):
    def __init__(self, cols, parent =  None):
        super(Desc_data, self).__init__(parent)
        self.setupUi(self)
        self.comboBox_2.addItems(cols)
        self.options = []
        self.comboBox_2.setVisible(False)
        self.label_2.setVisible(False)

        self.comboBox.currentTextChanged.connect(self.opt)

    def opt(self):
        if self.comboBox.currentText() != 'SELECT' and self.comboBox.currentText() != 'Headers' and self.comboBox.currentText() != 'Datatypes':
            self.comboBox_2.setVisible(True)
            self.label_2.setVisible(True)
        else:
            self.comboBox_2.setVisible(False)
            self.label_2.setVisible(False)

    def desc(self):
        self.options.append(self.comboBox.currentText())
        self.options.append(self.comboBox_2.currentText())
        self.accept()

class Histo_g(QtWidgets.QDialog, Ui_Hist):
    def __init__(self,cols, parent =  None):
        super(Histo_g, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.in_p)
        self.comboBox.addItems(cols)
        self.comboBox_2.addItems(cols)
        self.opt = []
        
    def in_p(self):
        self.opt.append(self.comboBox.currentText())
        self.opt.append(self.comboBox_2.currentText())
        self.accept()

class Feature(QtWidgets.QDialog, Ui_Feature_Tune):
    def __init__(self, cols , parent =  None):
        super(Feature, self).__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(cols)
        self.comboBox.currentTextChanged.connect(self.uniq)
        self.option = []
        self.buttonBox.accepted.connect(self.acc)
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

    def uniq(self):
        if self.comboBox.currentText() != 'SELECT':
            global df
            self.comboBox_2.clear()
            val = list(np.unique(df[self.comboBox.currentText()]))
            for i in range(0 , len(val)):
                val[i] = str(val[i])
            val = set(val)
            val = list(val)
            self.comboBox_2.addItem('SELECT')
            if 'nan' in val:
                self.comboBox_2.addItem('Null')
                val.remove('nan')
            val.sort()
            self.comboBox_2.addItems(val)
            self.label_2.setVisible(True)
            self.comboBox_2.setVisible(True)
            self.label_3.setVisible(True)
            self.lineEdit.setVisible(True)

    def acc(self):
        self.option.append(self.comboBox.currentText())
        self.option.append(self.comboBox_2.currentText())
        self.option.append(self.lineEdit.text())
        self.accept()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.browse_dlg)
        self.DisplayData.clicked.connect(self.r_data)
        self.EditData.currentTextChanged.connect(self.edit)
        self.DescribeDate.clicked.connect(self.desc)
        self.DropBox.currentTextChanged.connect(self.graphs)
        self.FeatureTuning.clicked.connect(self.feat)
        self.DisplayData.setDisabled(True)
        self.EditData.setDisabled(True)
        self.DescribeDate.setDisabled(True)
        self.FeatureTuning.setDisabled(True)
        self.DropBox.setDisabled(True)

    def browse_dlg(self):
        filename = QFileDialog.getOpenFileName()
        global f_path 
        f_path= filename[0]
        self.FilePath.setText(f_path)
        if f_path != "":
            try:
                global df
                df = pd.read_csv(f_path)
                global cols
                cols = df.columns.tolist()
                self.DisplayData.setDisabled(False)
                self.EditData.setDisabled(False)
                self.DescribeDate.setDisabled(False)
                self.FeatureTuning.setDisabled(False)
                self.DropBox.setDisabled(False)
            except:
                self.msg('File should be in \".csv\" format')
                self.FilePath.setText("")

    def msg(self, msg):
        q = QMessageBox()
        q.setIcon(QMessageBox.Critical)
        q.setWindowTitle('Error !!!')
        q.setText('Error while processing file')
        q.setInformativeText(msg)
        q.exec_()

    
    def r_data(self):
        global cols
        global df
        w = Dialog(cols)
        w.show()
        if w.exec_() == 1:
            try:      
                if(w.options[0] == 'Column Data'):
                    model = pandasModel(df[[w.options[1]]])
                    t = Table(model)
                    t.show()
                    t.exec_()
                else:
                    model = pandasModel(df)
                    t = Table(model)
                    t.show()
                    t.exec_()
            except:
                self.msg('Please select valid option !')

    def edit(self):
        global cols
        if self.EditData.currentIndex()!= 0:
            e = EditData(cols, self.EditData.currentText())
            e.show()
            if e.exec_() == 1:
                global df
                # print(e.opt)
                try:
                    if self.EditData.currentText() == 'One Hot Encode':
                        col = e.opt[0]
                        if df[col].dtypes != 'object':
                            self.msg('Column id not of type string')
                        else:
                            col_categories = np.unique(df[col])
                            # if len(col_categories) > 2:
                            #     print('\nThe Current Column contain ', len(col_categories)," !!!\nDo you wish to continue ? y/n", end = '')
                            #     c  = input()
                            try: 
                                ans = ""                            
                                for category in col_categories:
                                    category_series = df[col] == category
                                    category_feature = category_series.astype('int')
                                    df[col+ " " + category] = category_feature
                                    ans += " " + col+ " " + category
                                q = QMessageBox()
                                q.setIcon(QMessageBox.Information)
                                q.setWindowTitle('Successful')
                                q.setText('Column Categories')
                                q.setInformativeText(ans)
                                q.exec_()
                                # print(col_categories)
                                # print('\nCreated One Hot Encoded Columns with names : ')
                                # for category in col_categories:
                                #     print(col , ' ' , category)
                                # print('\nDo you wish to drop ',col, ' Column ? y/n')
                                # c  = input()
                                # if c == 'y' or c == 'Y':
                                df = df.drop(columns = col)
                                # print(df.columns.tolist())
                                cols = df.columns.tolist()
                            except:
                                print("\nSomething went wrong!!")
                    elif e.opt[2] == "":
                        if e.opt[1] == 'Delete Column':
                            df  = df.drop(columns=e.opt[0])
                            cols.remove(e.opt[0])
                        else:
                            df = df.dropna(axis= 0, subset=e.opt[0])
                            cols.remove(e.opt[0])
                    else:
                        if e.opt[3]  != 'SELECT':
                            d_type = df[e.opt[0]].dtypes
                            if d_type == 'object':
                                d_type = str
                            elif d_type == 'int64':
                                d_type = int
                            else :
                                d_type = float
                            key = (d_type) (e.opt[2])
                            print(key)
                            if e.opt[3] == 4:
                                cond = df[e.opt[0]] >= key
                            elif e.opt[3] == 5:
                                cond = df[e.opt[0]] <= key
                            elif e.opt[3] == 1:
                                cond = df[e.opt[0]] == key
                            elif e.opt[3] == 2:
                                cond = df[e.opt[0]] > key
                            else:
                                cond = df[e.opt[0]] < key
                            # print(len(df[cond][e.opt[0]].index))
                            df = df[~cond]
                except:
                    self.msg('Please select valid option !') 
                self.EditData.setCurrentIndex(0)

    def desc(self) :
        global cols
        global df
        d = Desc_data(cols)
        d.show()
        if d.exec_() == 1:
            if d.options[0] != 'SELECT':
                try:
                    if d.options[0] == 'Headers':
                        i = 1
                        ans = []
                        for i in range(0 , len(cols)):
                            ans.append(str("Column " + str(i+1)))
                        ans = {'Column' : cols, 'Headers' : ans }

                        temp  = pd.DataFrame.from_dict(ans)
                        model = pandasModel(temp)
                        t = Table(model)
                        t.show()
                        t.exec_()
                    elif d.options[0] == 'Column':
                        ans = dict(df[d.options[1]].describe())
                        temp = pd.DataFrame(list(ans.items()),columns = ['Parameter','Values'])
                        model = pandasModel(temp)
                        t = Table(model)
                        t.show()
                        t.exec_()
                    else:
                        ans = dict(df.dtypes)
                        temp = pd.DataFrame(list(ans.items()),columns = ['Parameter','Values'])
                        model = pandasModel(temp)
                        t = Table(model)
                        t.show()
                        t.exec_()
                except:
                    self.msg('Please select valid option !')

    def graphs(self):
        if self.DropBox.currentText() != 'SELECT':
            global df
            global cols
            if self.DropBox.currentText() == 'Histogram':
                h = Histo_g(cols)
                h.show()
                if h.exec_() == 1:
                    try: 
                        labels = np.unique(df[h.opt[0]])
                        # print(labels, '\n', len(labels))
                        x = list()
                        for i,label in enumerate(labels):
                            # print('label = ', label, '  i =  ', i)
                            x.append(df[df[h.opt[0]] == label][h.opt[1]])
                            # print('\n\n\nValues = ',x[i])
                        kwargs = dict(edgecolor= 'black')
                        fig, ax = plt.subplots()
                        for i in range(0, len(x)):
                            ax.hist(x[i].values, **kwargs)
                            # print(x[i].values)
                        ax.legend(labels, loc = "upper right", title = h.opt[0])
                        ax.set_title(h.opt[1])
                        ax.set_xlabel('Column Values')
                        ax.set_ylabel("No. of Entries")
                        plt.show()
                    except:
                        self.msg('\nSomething went Wrong!!!')
            elif self.DropBox.currentText() == 'Correlation Data':
                plt.figure(figsize= (8,8))
                temp = df
                for col in cols:
                    if len(df[col].unique()) == 1:
                        temp = temp.drop(col,axis=1)
                seaborn.heatmap(df.corr(), annot = True, cmap = 'coolwarm').set_title('Correlation Data')
                plt.show()
            self.DropBox.setCurrentIndex(0)

    def feat(self):
        global cols
        f  = Feature(cols)
        f.show()
        if f.exec_() == 1:
            global df
            # print(f.option)
            try:
                d_type = df[f.option[0]].dtypes
                if d_type == 'object':
                    d_type = str
                elif d_type == 'int64':
                    d_type = int
                else :
                    d_type = float
                key = (d_type) (f.option[2])
                if f.option[1] != 'Null':
                    rep = (d_type ) (f.option[1])
                    df.loc[df[f.option[0]] == rep, f.option[0] ] = key
                # print('rep => ', rep, 'key => ', key, 'dtype => ', d_type)
                else:
                    df[f.option[0]] = df[f.option[0]].fillna(key)
            except:
                self.msg('Please select valid option !')

    def SaveDF(self):
        global df
        if not(df.empty):
            with open("DataFrame\\DataFrame.pickle","wb") as f:
                pickle.dump(df, f)


import Images_rc


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())