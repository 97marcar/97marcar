import sys #system
from PyQt4.QtCore import * #importing all QtCore functions
from PyQt4.QtGui import * #importing all QtGui functions
import model

app = QApplication(sys.argv)

class Register(QMainWindow):
    
    def __init__(self, parent=None):
        """The constructor of the Register class, the main class."""
        super(Register, self).__init__()
        self.setWindowTitle("Test")
        self.initUI()
    
    
    def initUI(self):
        """Here you create every GUI component(everything you see)"""
        pass
        
    def run(self):
        self.show()
        sys.exit(app.exec_())
        
Register().run()