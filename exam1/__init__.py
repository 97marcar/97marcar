
import sys #system

from PyQt4.QtCore import * #importing all QtCore functions
from PyQt4.QtGui import * #importing all QtGui functions
from model import *

app = QApplication(sys.argv)

model = Model()
selectedFormat = "Blueray"

class Register(QMainWindow):
    
    def __init__(self, parent=None):
        """The constructor of the Register class, the main class."""
        super(Register, self).__init__()
        self.setWindowTitle("Register")
        self.setGeometry(300, 30, 700, 600)
        self.initUI()
        model.get_saveBR()
        model.get_saveDVD()
        model.get_saveVHS()
        self.updateBR()
        self.updateDVD()
        self.updateVHS()
        
        
    
    def initUI(self):
        """Here you create every GUI component(everything you is see)"""
        #creates a QWidget
        self.frame = QWidget(self) 
        
        #set the Central Widget to the QWidget
        self.setCentralWidget(self.frame)
        
        #Creates a Vertical boxlayout 
        self.layout = QVBoxLayout()
        
        #Creates a gridlayout and adds it to the VBoxLayout
        self.gridlayout = QGridLayout()
        self.layout.addLayout(self.gridlayout)
        self.gridlayout.setSpacing(10)
        
        #Adds the objects to the gridlayout
        self.gridlayout.addWidget(QLabel("Format"), 1, 0)
        self.gridlayout.addWidget(QLabel("Name"), 1, 1)
        self.gridlayout.addWidget(QLabel("Genre"), 1, 2)
        self.gridlayout.addWidget(QLabel("Director"), 1, 3)
        self.gridlayout.addWidget(QLabel("Year"), 1, 4)
        self.gridlayout.addWidget(QLabel("Res, Length or Color"), 1, 5)
        
        #Creates a topmenu
        self.topmenu = self.menuBar()
        self.about = self.topmenu.addMenu("About")
        self.aboutText = QAction("Made by Marcus Carlsson", self)
        self.about.addAction(self.aboutText)
        
        #Creates a Text Edit window(can come to change)
        self.mainWindow0 = QTextEdit()
        self.mainWindow1 = QTextEdit()
        self.mainWindow2 = QTextEdit()
        self.mainWindow3 = QTextEdit()
        self.mainWindow4 = QTextEdit()
        self.mainWindow5 = QTextEdit()
        
        #adds the mainWindow to the layout
        self.gridlayout.addWidget(self.mainWindow0, 2, 0)
        self.gridlayout.addWidget(self.mainWindow1, 2, 1)
        self.gridlayout.addWidget(self.mainWindow2, 2, 2)
        self.gridlayout.addWidget(self.mainWindow3, 2, 3)
        self.gridlayout.addWidget(self.mainWindow4, 2, 4)
        self.gridlayout.addWidget(self.mainWindow5, 2, 5)
        self.mainWindow0.setReadOnly(True)
        self.mainWindow1.setReadOnly(True)
        self.mainWindow2.setReadOnly(True)
        self.mainWindow3.setReadOnly(True)
        self.mainWindow4.setReadOnly(True)
        self.mainWindow5.setReadOnly(True)

        
        #Applies the layout to the frame
        self.frame.setLayout(self.layout)
        
        #Creates a dropdown menu so you can choose format
        self.dropDown = QComboBox(self)
        self.dropDown.addItem("Blueray")
        self.dropDown.addItem("DVD")
        self.dropDown.addItem("VHS")
        self.gridlayout.addWidget(self.dropDown, 3, 0)
        self.dropDown.activated[str].connect(self.whenActivated)
        
        #Creates the "Add" button to the window
        self.btn_add = QPushButton('Add', self)
        self.btn_add.clicked.connect(self.btn_add_action)
        self.gridlayout.addWidget(self.btn_add,3, 1)
        
        self.spinbox = QSpinBox()
        self.spinbox.setMaximum(9999)
        self.gridlayout.addWidget(self.spinbox, 3, 2)        
        
        self.btn_edit = QPushButton('Edit', self)
        self.btn_edit.clicked.connect(self.btn_edit_action)
        self.gridlayout.addWidget(self.btn_edit, 3, 3)
        
        self.btn_remove = QPushButton('Remove', self)
        self.btn_remove.clicked.connect(self.btn_remove_action)
        self.gridlayout.addWidget(self.btn_remove, 3, 4)
        
        
    def whenActivated(self, itemFormat):
        global selectedFormat
        selectedFormat = itemFormat
        
    def updateBR(self):
        self.mainWindow0.clear()
        self.mainWindow1.clear()
        self.mainWindow2.clear()
        self.mainWindow3.clear()
        self.mainWindow4.clear()
        self.mainWindow5.clear()
        
        lista = model.get_itemsBR()
            
        for item in lista:
            self.mainWindow0.append(item.movie_type)
            self.mainWindow1.append(item.name) 
            self.mainWindow2.append(item.genre)
            self.mainWindow3.append(item.director)
            self.mainWindow4.append(item.year)
            self.mainWindow5.append(item.resolution)
    
    def updateDVD(self):        
        lista = model.get_itemsDVD()
            
        for item in lista:
            self.mainWindow0.append(item.movie_type)
            self.mainWindow1.append(item.name) 
            self.mainWindow2.append(item.genre)
            self.mainWindow3.append(item.director)
            self.mainWindow4.append(item.year)
            self.mainWindow5.append(item.length)
            
    def updateVHS(self):        
        lista = model.get_itemsVHS()
            
        for item in lista:
            self.mainWindow0.append(item.movie_type)
            self.mainWindow1.append(item.name) 
            self.mainWindow2.append(item.genre)
            self.mainWindow3.append(item.director)
            self.mainWindow4.append(item.year)
            self.mainWindow5.append(item.color)
         
    def btn_add_action(self):
        """..."""
        self.popup = PopUpWindow()
        self.popup.edit = False
        self.popup.exec_()
        
    def btn_edit_action(self):
        """..."""
        self.popup = PopUpWindow(edit=True)
        self.popup.exec_()
        
    def btn_remove_action(self):
        """..."""
        self.remove_value = self.spinbox.value()
        if selectedFormat == "Blueray":
            model.lista_BR.pop(int(self.remove_value)-1)
        elif selectedFormat == "DVD":
            model.lista_DVD.pop(int(self.remove_value)-1)
        elif selectedFormat == "VHS":
            model.lista_VHS.pop(int(self.remove_value)-1)
        self.updateBR()
        self.updateDVD()
        self.updateVHS()
        model.set_saveBR()
        model.set_saveDVD()
        model.set_saveVHS()
  
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        
register = Register()

class PopUpWindow(QDialog):
    def __init__(self, parent=None, edit=False):
        super(PopUpWindow, self).__init__(parent)
        self.setGeometry(300, 30, 700, 600)
        self.edit = edit
        self.dialogUI()
        self.setWindowTitle(selectedFormat)
        
        
    def dialogUI(self):
        
        self.Dlayout = QGridLayout(self)
        self.Dlayout.setSpacing(10)
                
        self.addName = QLabel("Name: ")
        self.addNameText = QLineEdit()
        self.addGenre = QLabel("Genre: ")
        self.addGenreText = QLineEdit()
        self.addDirector = QLabel("Director: ")
        self.addDirectorText = QLineEdit()
        self.addYear = QLabel("Year: ")
        self.addYearText = QLineEdit()
        if selectedFormat == "DVD":
            self.addUnique = QLabel("Length: ")
        elif selectedFormat == "Blueray":
            self.addUnique = QLabel("Resolution: ")
        elif selectedFormat == "VHS":
            self.addUnique = QLabel("Color?: ")
        self.addUniqueText = QLineEdit()
        
        if self.edit == True:
            if selectedFormat == "Blueray":
                self.addNameText.setText(model.lista_BR[register.spinbox.value()-1].name)
                self.addGenreText.setText(model.lista_BR[register.spinbox.value()-1].genre)
                self.addDirectorText.setText(model.lista_BR[register.spinbox.value()-1].director)
                self.addYearText.setText(model.lista_BR[register.spinbox.value()-1].year)
                self.addUniqueText.setText(model.lista_BR[register.spinbox.value()-1].resolution)
            if selectedFormat == "DVD":
                self.addNameText.setText(model.lista_DVD[register.spinbox.value()-1].name)
                self.addGenreText.setText(model.lista_DVD[register.spinbox.value()-1].genre)
                self.addDirectorText.setText(model.lista_DVD[register.spinbox.value()-1].director)
                self.addYearText.setText(model.lista_DVD[register.spinbox.value()-1].year)
                self.addUniqueText.setText(model.lista_DVD[register.spinbox.value()-1].length)
            if selectedFormat == "VHS":
                self.addNameText.setText(model.lista_VHS[register.spinbox.value()-1].name)
                self.addGenreText.setText(model.lista_VHS[register.spinbox.value()-1].genre)
                self.addDirectorText.setText(model.lista_VHS[register.spinbox.value()-1].director)
                self.addYearText.setText(model.lista_VHS[register.spinbox.value()-1].year)
                self.addUniqueText.setText(model.lista_VHS[register.spinbox.value()-1].color)
        
        self.btnQDialog = QPushButton("Add", self)
        self.btnQDialog.clicked.connect(self.btnQDialog_action)
        
        self.Dlayout.addWidget(self.addName, 1, 0)
        self.Dlayout.addWidget(self.addNameText, 1, 1)
        self.Dlayout.addWidget(self.addGenre, 2, 0)
        self.Dlayout.addWidget(self.addGenreText, 2, 1)  
        self.Dlayout.addWidget(self.addDirector, 3, 0)
        self.Dlayout.addWidget(self.addDirectorText, 3, 1)  
        self.Dlayout.addWidget(self.addYear, 4, 0)
        self.Dlayout.addWidget(self.addYearText, 4, 1)  
        self.Dlayout.addWidget(self.addUnique, 5, 0)
        self.Dlayout.addWidget(self.addUniqueText, 5, 1)
        self.Dlayout.addWidget(self.btnQDialog, 6, 1)

    def btnQDialog_action(self):
        self.stringName = str(self.addNameText.text())
        self.stringGenre = str(self.addGenreText.text())
        self.stringDirector = str(self.addDirectorText.text())
        self.stringYear = str(self.addYearText.text())
        self.stringUnique = str(self.addUniqueText.text())
        
        if self.edit == False:
            model.create_item(selectedFormat, self.stringUnique, self.stringName, \
            self.stringGenre, self.stringDirector, self.stringYear)

        elif self.edit == True:
            model.edit_item(selectedFormat, self.stringUnique, self.stringName, \
            self.stringGenre, self.stringDirector, self.stringYear, register.spinbox.value()-1)
            
        
        register.updateBR()
        register.updateDVD()
        register.updateVHS()
        model.set_saveBR()
        model.set_saveDVD()
        model.set_saveVHS()
        
     
        
        

    
register.run()