
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
        self.label_layout = QGridLayout()
        self.layout.addLayout(self.label_layout)
        self.label_layout.setSpacing(10)
        
        #Adds the objects to the gridlayout
        self.label_layout.addWidget(QLabel("Format"), 1, 0)
        self.label_layout.addWidget(QLabel("Name"), 1, 1)
        self.label_layout.addWidget(QLabel("Genre"), 1, 2)
        self.label_layout.addWidget(QLabel("Director"), 1, 3)
        self.label_layout.addWidget(QLabel("Year"), 1, 4)
        self.label_layout.addWidget(QLabel("Res, Length or Color"), 1, 5)
        
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
        self.label_layout.addWidget(self.mainWindow0, 2, 0)
        self.label_layout.addWidget(self.mainWindow1, 2, 1)
        self.label_layout.addWidget(self.mainWindow2, 2, 2)
        self.label_layout.addWidget(self.mainWindow3, 2, 3)
        self.label_layout.addWidget(self.mainWindow4, 2, 4)
        self.label_layout.addWidget(self.mainWindow5, 2, 5)
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
        self.layout.addWidget(self.dropDown)
        self.dropDown.activated[str].connect(self.whenActivated)
        
        #Creates the "Add" button to the window
        self.btn_add = QPushButton('Add', self)
        self.btn_add.clicked.connect(self.btn_add_action)
        self.layout.addWidget(self.btn_add)
        
        self.btn_restore = QPushButton('restore', self)
        self.btn_restore.clicked.connect(self.btn_restore_action)
        self.layout.addWidget(self.btn_restore)
        
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
        self.popup.exec_()
        
    def btn_restore_action(self):
        """..."""
        model.get_saveBR()
        model.get_saveDVD()
        model.get_saveVHS()
        register.updateBR()
        register.updateDVD()
        register.updateVHS()
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        
register = Register()

class PopUpWindow(QDialog):
    def __init__(self, parent=None):
        super(PopUpWindow, self).__init__(parent)
        self.setGeometry(300, 30, 700, 600)
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
        
        model.create_item(selectedFormat, self.stringUnique, self.stringName, self.stringGenre, self.stringDirector, self.stringYear)
        register.updateBR()
        register.updateDVD()
        register.updateVHS()
        model.set_saveBR()
        model.set_saveDVD()
        model.set_saveVHS()
        
     
        
        

    
register.run()