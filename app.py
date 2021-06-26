import csv
import os
import sys
import numpy as np
from decimal import Decimal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

from mainwindow import Ui_MainWindow


class MainWindowUIClass(Ui_MainWindow):

    def __init__(self):
        super().__init__()

    def setupUi(self, MW):
        super().setupUi(MW)
        self.btn_Set.clicked.connect(lambda: self.find())
        self.btn_calc.clicked.connect(lambda: self.readData())
        self.final_matrix = []
        _translate = QtCore.QCoreApplication.translate

    def find(self):
        # finding the content of current items in combo box
        row = self.rows.currentText()
        column = self.cloumns.currentText()
        print('test ' + row, column)
        # Writing the names of the labels in the table
        labels = []
        for i in range(int(column)):
            labels.append('X' + str(i))
        print(labels)
        # Setting up the rows and columns
        self.tableWidget.setRowCount(int(row))
        self.tableWidget.setColumnCount(int(column))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        item = self.tableWidget.horizontalHeaderItem(int(column) - 1)
        item.setText("b")
        print(self.final_matrix)

    def readData(self):
        rowCount = self.tableWidget.rowCount()
        cloumnCount = self.tableWidget.columnCount()
        lst_table = []

        for row in range(rowCount):
            rowData = ''
            for column in range(cloumnCount):
                widgetItem = self.tableWidget.item(row, column)
                print(widgetItem.text())
                lst_table.append(widgetItem.text())

        print(lst_table)
        matrix = []
        while lst_table != []:
            matrix.append(lst_table[:cloumnCount])
            lst_table = lst_table[cloumnCount:]
        print(matrix)
        mat2 = [list(map(int, x)) for x in matrix]
        print(mat2)
        self.final_matrix = mat2
        self.luDecomposition(mat2, rowCount)

    def luDecomposition(self, mat, n):
        lower = [[0 for x in range(n)]
                 for y in range(n)]
        upper = [[0 for x in range(n)]
                 for y in range(n)]

        # Decomposing matrix into Upper
        # and Lower triangular matrix
        for i in range(n):

            # Upper Triangular
            for k in range(i, n):

                # Summation of L(i, j) * U(j, k)
                sum = 0
                for j in range(i):
                    sum += (lower[i][j] * upper[j][k])

                    print(('lower[', i, '][', j, '] * upper[', j, '][', k, ']'))
                # Evaluating U(i, k)
                upper[i][k] = mat[i][k] - sum

            # Lower Triangular
            for k in range(i, n):
                if (i == k):
                    lower[i][i] = 1  # Diagonal as 1
                else:

                    # Summation of L(k, j) * U(j, i)
                    sum = 0
                    for j in range(i):
                        sum += (lower[k][j] * upper[j][i])

                    # Evaluating L(k, i)
                    lower[k][i] = round(Decimal((mat[k][i] - sum) /
                                                upper[i][i]), 2)
        # setw is for displaying nicely
        print("Lower Triangular")
        print(np.array(lower))
        print("Upper Triangular")
        print(np.array(upper))

 

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
