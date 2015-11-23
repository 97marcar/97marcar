
import sys #system

from PyQt4.QtCore import * #importing all QtCore functions
from PyQt4.QtGui import * #importing all QtGui functions
from model import *

app = QApplication(sys.argv)

model = Model()

class Register(QMainWindow):
    
    def __init__(self, parent=None):
        """The constructor of the Register class, the main class."""
        super(Register, self).__init__()
        self.setWindowTitle("Register")
        self.setGeometry(300, 30, 700, 600)
        self.initUI()
        self.popup = PopUpWindow()
    
    def initUI(self):
        """Here you create every GUI component(everything you is see)"""
        #creates a QWidget
        self.frame = QWidget(self) 
        #set the Central Widget to the QWidget
        self.setCentralWidget(self.frame)
        
        #Creates a Vertical boxlayout 
        self.layout = QVBoxLayout() 
        
        #Creates a Text Edit window(can come to change)
        self.mainWindow = QTextEdit()
        #adds the mainWindow to the layout
        self.layout.addWidget(self.mainWindow)
        self.mainWindow.setReadOnly(True)
        
        #Creates a Line edit where the user input data.
        self.userInput = QLineEdit() 
        #adds the userInput to the layout
        self.layout.addWidget(self.userInput) 
        
        #Applies the layout to the frame
        self.frame.setLayout(self.layout)
        
        #Creates the "Add" button to the window
        self.btn_add = QPushButton('Add', self)
        self.btn_add.clicked.connect(self.btn_add_action)
        self.layout.addWidget(self.btn_add)
         
    def btn_add_action(self):
        """..."""
        self.popup.exec_()
        
    def run(self):
        self.show()
        sys.exit(app.exec_())

class PopUpWindow(QDialog):
    def __init__(self, parent=None):
        super(PopUpWindow, self).__init__(parent)
        self.setGeometry(300, 30, 700, 600)
        self.dialogUI()
        
        
    def dialogUI(self):
        self.Dlayout = QGridLayout(self)
        pos = [(0, 0), (0, 1),
               (1, 0), (1, 1),
                (2, 0), (2, 2),
                (3, 0), (3, 3),
                (4, 0), (4, 4),
                (5, 0), (5, 5),
                (6, 0), (6, 6),
                (7, 0), (7, 7),
                (8, 0), (8, 8),
                (9, 0), (9, 9),
                (10, 0), (10, 10)]
                
        self.addName = QLabel("Name: ")
        self.addNameText = QLineEdit()
        self.addGenre = QLabel("Genre: ")
        self.addGenreText = QLineEdit()
        self.addDirector = QLabel("Director: ")
        self.addDirectorText = QLineEdit()
        self.addYear = QLabel("Year: ")
        self.addYearText = QLineEdit()
        if model.item.movie_type == "DVD":
            self.addUnique = QLabel("Length: ")
            self.addUniqueText = QLineEdit()
        elif self.model.item.movie_type == "BR":
            self.addUnique = QLabel("Resolution: ")
            self.addUniqueText = QLineEdit()
        elif self.model.item.movie_type == "VHS":
            self.addUnique = QLabel("Color?: ")
            self.addUniqueText = QLineEdit()
        self.btnQDialog = QPushButton("Add", self)
        self.btnQDialog.clicked.connect(self.btnQDialog_action)
            
        self.Dlayout.addWidget(self.addName, pos[0][0], pos[0][1])
        self.Dlayout.addWidget(self.addNameText, pos[1][0], pos[1][1])
        self.Dlayout.addWidget(self.addGenre, pos[2][0], pos[0][1])
        self.Dlayout.addWidget(self.addGenreText, pos[2][0], pos[1][1])  
        self.Dlayout.addWidget(self.addDirector, pos[4][0], pos[0][1])
        self.Dlayout.addWidget(self.addDirectorText, pos[4][0], pos[1][1])  
        self.Dlayout.addWidget(self.addYear, pos[6][0], pos[0][1])
        self.Dlayout.addWidget(self.addYearText, pos[6][0], pos[1][1])  
        self.Dlayout.addWidget(self.addUnique, pos[8][0], pos[0][1])
        self.Dlayout.addWidget(self.addUniqueText, pos[8][0], pos[1][1])
        self.Dlayout.addWidget(self.btnQDialog, pos[10][0], pos[1][1])

    def btnQDialog_action(self):
        print("123")
        
     
        
        

    
Register().run()