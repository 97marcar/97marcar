
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
        self.btn_add= QPushButton('Add', self)
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
        self.dialogUI()
        
    def dialogUI(self):
        self.Dlayout = QVBoxLayout(self)
        self.addName = QLabel()
        self.addNameText = QLineEdit()
        self.Dlayout.addWidget(self.addName)
        self.Dlayout.addWidget(self.addNameText)   

        
     
        
        

        
Register().run()