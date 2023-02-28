import sys

from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
PLS = ""
d = dict()
d[1] = d[2] = d[3] = []
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pls.clicked.connect(self.plsbrowser)
        self.submit.clicked.connect(self.submitfunc)
        self.display.clicked.connect(self.displayfunc)
        self.generate.clicked.connect(self.generatefunc)
    def plsbrowser(self):
        global PLS
        path,_=QFileDialog.getOpenFileNames()
        path=path[0]

        f = open(path,'r')
        PLS=f.read()
        self.labelpls.setText(path[path.rfind('/')+1:])

    def submitfunc(self):
        global d
        # take values

        A = self.arange.text()
        B = self.brange.text()
        C = self.crange.text()
        M1 = self.metal1.text()
        M2 = self.metal2.text()
        M3 = self.metal3.text()

        # save them in  d[i]
        if self.block1.isChecked():
            i = 1
            self.labela1.setText(A)
            self.labela2.setText(B)
            self.labela3.setText(C)
            self.labelm1.setText(M1)
            self.labelm2.setText(M2)
            self.labelm3.setText(M3)
        elif self.block2.isChecked():
            i = 2
            self.labelb1.setText(A)
            self.labelb2.setText(B)
            self.labelb3.setText(C)
            self.labeln1.setText(M1)
            self.labeln2.setText(M2)
            self.labeln3.setText(M3)
        elif self.block3.isChecked():
            i = 3
            self.labelc1.setText(A)
            self.labelc2.setText(B)
            self.labelc3.setText(C)
            self.labell1.setText(M1)
            self.labell2.setText(M2)
            self.labell3.setText(M3)

        d[i] = [PLS, A, B, C, M1, M2, M3]
        self.labelsubmit.setText("valid submition for block {}".format(i))
    def displayfunc(self):
        ch=""
        for i  in range(1,4):
            if len(d[i])!=0:
                ch+="information about the block "+str(i)+" : \n"
                ch+="PLS name is : "+d[i][0]+" .\n"
                ch += "Ranges are : [" + d[i][1] +" ; "+d[i][2]+"[  , ["+ d[i][2] +" ; "+d[i][3]+"[  ,  ["+  d[i][3] +" ; infini [ "   + ".\n"
                ch +="Metals are : "+d[i][4]+","+d[i][5]+" and "+d[i][6] +".\n \n"
            else :
                ch+= " the block "+str(i)+" is empty \n \n"
        self.labeldisplay.setFont(QFont('Times', 10))
        self.labeldisplay.setText(ch)
    def generatefunc(self):
        global d
        #pls
        print(d)
        ch="namespace spectrum;\n{\n\n    class treedecision { \n        private static readonly double[] PLS1 = new double[]{"+d[1][0]+"}\n        private static readonly double[] PLS2 = new double[]{"+d[2][0]+"}\n        private static readonly double[] PLS3 = new double[]{"+d[3][0]+"}\n"
        ch+="        private static readonly double[] data = new double[]{}\n        private static readonly int length =48;\n        static void Main(string[] args)\n        {"
        #ranges
        ch+="           int a1,a2,a3,b1,b2,b3,c1,c2,c3;\n"
        ch+="           a1="+d[1][1]+";a2="+d[1][2]+";a3="+d[1][3]+";b1="+d[2][1]+";b2="+d[2][2]+";b3="+d[2][3]+";c1="+d[3][1]+";c2="+d[3][2]+";c3="+d[3][3]+";\n"
        ch+="           double score =0;\n           for(int spec=0;spec<length;spec++) score+=PLS1[spec]*data[spec];\n           if(a1<=score && score <a2){\n            score =0;\n            for(int spec=0;spec<length;spec++) score+=PLS2[spec]*data[spec];\n            if(b1<=score && score <b2){\n"
        #metals
        ch+="                    System.Console.WriteLine(\""+d[2][4]+"\");}\n            else if(b2<=score && score <b3) {\n"
        ch+="                    System.Console.WriteLine(\""+d[2][5]+"\");}\n            else {System.Console.WriteLine(\""+d[2][6]+"\");}\n           }\n            else if(a2<=score && score <a3){\n            score =0;\n"
        ch+="            for(int spec=0;spec<length;spec++) score+=PLS3[spec]*data[spec];\n            if(c1<=score && score <c2){\n                    System.Console.WriteLine(\""+d[3][4]+"\");}\n            else if(c2<=score && score <c3) {\n"
        ch+="                    System.Console.WriteLine(\""+d[3][5]+"\");}\n            else {System.Console.WriteLine(\""+d[3][6]+"\");}\n"
        ch+="           }\n\n        }\n    }\n}"
        print(ch)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

""" 
class designWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.submit.clicked.connect(self.submitfunc)
        #self.show.clicked.connect(self.CompressedImg)
        #self.generate.clicked.connect(self.showSimilarImages)

    def submitfunc(self):
        # 5oudh l indice mta3 dictionaire mel block
        # 5oudh les valeurs l o5rin
        PLS=self.pls.LineEdit.text()
        #3ammer d[i]
        print(PLS)








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = designWindow()
    window.show()
    sys.exit(app.exec_())
"""
