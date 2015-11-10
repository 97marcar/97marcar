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
        self.frame = QWidget(self) #creates a QWidget
        self.setCentralWidget(self.frame) #set the Central Widget to the QWidget
        
        self.layout = QVBoxLayout() #Creates a Vertical boxlayout 
        
        self.mainWindow = QTextEdit() #Creates a Text Edit window(can come to change)
        self.layout.addWidget(self.mainWindow) #adds the mainWindow to the layout
        self.mainWindow.setReadOnly(True)
        
        self.userInput = QLineEdit() #Creates a Line edit where the user input data.
        self.layout.addWidget(self.userInput) #adds the userInput to the layout
        
        self.frame.setLayout(self.layout) #Applies the layout to the frame
        
        
        
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        
Register().run()