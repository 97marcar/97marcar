import sys #system
from PyQt4.QtCore import * #importing all QtCore functions
from PyQt4.QtGui import * #importing all QtGui functions
import model

app = QApplication(sys.argv)

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
        self.btn_add= QPushButton('Add', self)
        self.btn_add.clicked.connect(self.btn_add_action)
        self.layout.addWidget(self.btn_add)
        
        
        
    def btn_add_action(self):
        """..."""
        self.addmovie_frame = QDialog()
        self.addmovie_frame.exec_()
        
        
        #Get this to work on a Dialog(this is code for a QWidget)
        """
        self.addmovie_layout = QGridLayout()
        pos = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2)]
        self.addName = QLabel()
        self.addNameText = QLineEdit()
        self.addmovie_layout.addWidget(self.addName, pos[0][0], pos[0][1])
        self.addmovie_layout.addWidget(self.addName, pos[1][0], pos[1][1])
        self.show()"""
       
        
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        
Register().run()