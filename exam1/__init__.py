
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
        
    
    def initUI(self):
        """Here you create every GUI component(everything you is see)"""
        #creates a QWidget
        self.frame = QWidget(self) 
        
        #set the Central Widget to the QWidget
        self.setCentralWidget(self.frame)
        
        #Creates a Vertical boxlayout 
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Format"+2*"\t"+"Name"+2*"\t"+\
        "Genre"+2*"\t"+"Director"+2*"\t"+"Year"+2*"\t"+"Res, Length or Color"))
        
        #Creates a topmenu
        self.topmenu = self.menuBar()
        self.about = self.topmenu.addMenu("About")
        self.aboutText = QAction("Made by Marcus Carlsson", self)
        self.about.addAction(self.aboutText)
        
        #Creates a Text Edit window(can come to change)
        self.mainWindow = QTextEdit()
        
        #adds the mainWindow to the layout
        self.layout.addWidget(self.mainWindow)
        self.mainWindow.setReadOnly(True)
        
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
        
    def whenActivated(self, itemFormat):
        global selectedFormat
        selectedFormat = itemFormat
        
    def update(self):
        self.mainWindow.clear()
        lista = model.get_item()
        for item in lista:
            self.mainWindow.append(item.movie_type + "\t" + \
            item.name + "\t" + item.genre + "\t" + \
            item.director + "\t" + item.year + "\t" + \
            item.resolution)
         
    def btn_add_action(self):
        """..."""
        self.popup = PopUpWindow()
        self.popup.exec_()
        
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
        register.update()
        
     
        
        

    
register.run()