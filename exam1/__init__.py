
import sys #system

from PyQt4.QtCore import * #importing all QtCore functions
from PyQt4.QtGui import * #importing all QtGui functions
from model import *

app = QApplication(sys.argv)

model = Model()
selectedFormat = "Blueray"

class Register(QMainWindow):
    """A class that creates the main window for a register"""
    
    def __init__(self, parent=None):
        """The constructor of the Register class, the main class."""
        super(Register, self).__init__()
        self.setWindowTitle("Register")
        self.setGeometry(300, 30, 700, 600)
        self.initUI()
        model.get_saveBR()
        model.get_saveDVD()
        model.get_saveVHS()
        self.clear_mainWindows()
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
        
        #Adds the search label and lineedit        
        self.search = QLineEdit()
        self.gridlayout.addWidget(QLabel("\t\tSearch:"), 1, 4)
        self.gridlayout.addWidget(self.search, 1, 5)
        self.search.returnPressed.connect(self.search_action)
        
        #Adds the objects to the gridlayout
        self.gridlayout.addWidget(QLabel("Format"), 2, 0)
        self.gridlayout.addWidget(QLabel("Name"), 2, 1)
        self.gridlayout.addWidget(QLabel("Genre"), 2, 2)
        self.gridlayout.addWidget(QLabel("Director"), 2, 3)
        self.gridlayout.addWidget(QLabel("Year"), 2, 4)
        self.gridlayout.addWidget(QLabel("Res, Length or Color"), 2, 5)
        
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
        self.gridlayout.addWidget(self.mainWindow0, 3, 0)
        self.gridlayout.addWidget(self.mainWindow1, 3, 1)
        self.gridlayout.addWidget(self.mainWindow2, 3, 2)
        self.gridlayout.addWidget(self.mainWindow3, 3, 3)
        self.gridlayout.addWidget(self.mainWindow4, 3, 4)
        self.gridlayout.addWidget(self.mainWindow5, 3, 5)
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
        self.gridlayout.addWidget(self.dropDown, 4, 0)
        self.dropDown.activated[str].connect(self.whenActivated)
        
        #Creates the "Add" button to the window
        self.btn_add = QPushButton('Add', self)
        self.btn_add.clicked.connect(self.btn_add_action)
        self.gridlayout.addWidget(self.btn_add, 4, 1)
        
        #Creates spinbox and adds it to the layout
        self.spinbox = QSpinBox()
        self.spinbox.setMaximum(9999)
        self.gridlayout.addWidget(self.spinbox, 4, 2)        
        
        #Creates a edit button and adds it to the layout
        self.btn_edit = QPushButton('Edit', self)
        self.btn_edit.clicked.connect(self.btn_edit_action)
        self.gridlayout.addWidget(self.btn_edit, 4, 3)
        
        #Creates a remove button and adds it to the layout
        self.btn_remove = QPushButton('Remove', self)
        self.btn_remove.clicked.connect(self.btn_remove_action)
        self.gridlayout.addWidget(self.btn_remove, 4, 4)
        
        
    def whenActivated(self, itemFormat):
        """Changes selectedFormat to itemFormat"""
        global selectedFormat
        selectedFormat = itemFormat
        
    def clear_mainWindows(self):
        """clears all of the main windows"""
        self.mainWindow0.clear()
        self.mainWindow1.clear()
        self.mainWindow2.clear()
        self.mainWindow3.clear()
        self.mainWindow4.clear()
        self.mainWindow5.clear()
        
    def updateBR(self):
        """Applies the new (and old) Blueray movies to the mainwindows"""        
        lista = model.get_itemsBR()
            
        for item in lista:
            self.mainWindow0.append(item.movie_type)
            self.mainWindow1.append(item.name) 
            self.mainWindow2.append(item.genre)
            self.mainWindow3.append(item.director)
            self.mainWindow4.append(item.year)
            self.mainWindow5.append(item.resolution)
    
    def updateDVD(self):
        """Applies the new (and old) DVD movies to the mainwindows"""        
        lista = model.get_itemsDVD()
            
        for item in lista:
            self.mainWindow0.append(item.movie_type)
            self.mainWindow1.append(item.name) 
            self.mainWindow2.append(item.genre)
            self.mainWindow3.append(item.director)
            self.mainWindow4.append(item.year)
            self.mainWindow5.append(item.length)
            
    def updateVHS(self):
        """Applies the new (and old) VHS movies to the mainwindows"""        
        lista = model.get_itemsVHS()
            
        for item in lista:
            self.mainWindow0.append(item.movie_type)
            self.mainWindow1.append(item.name) 
            self.mainWindow2.append(item.genre)
            self.mainWindow3.append(item.director)
            self.mainWindow4.append(item.year)
            self.mainWindow5.append(item.color)
            
    def search_action(self):
        """Search the lists and appends the found results to the mainWindow"""
        text = self.search.text()
        self.clear_mainWindows()
        listaBR = model.get_itemsBR()
        listaDVD = model.get_itemsDVD()
        listaVHS = model.get_itemsVHS()
        for item in listaBR:
            if text in item.name or text in item.genre or text in item.director or \
            text in item.year or text in item.resolution:
                self.mainWindow0.append(item.movie_type)
                self.mainWindow1.append(item.name) 
                self.mainWindow2.append(item.genre)
                self.mainWindow3.append(item.director)
                self.mainWindow4.append(item.year)
                self.mainWindow5.append(item.resolution)
        for item in listaDVD:
            if text in item.name:
                self.mainWindow0.append(item.movie_type)
                self.mainWindow1.append(item.name) 
                self.mainWindow2.append(item.genre)
                self.mainWindow3.append(item.director)
                self.mainWindow4.append(item.year)
                self.mainWindow5.append(item.length)
        for item in listaVHS:
            if text in item.name:
                self.mainWindow0.append(item.movie_type)
                self.mainWindow1.append(item.name) 
                self.mainWindow2.append(item.genre)
                self.mainWindow3.append(item.director)
                self.mainWindow4.append(item.year)
                self.mainWindow5.append(item.color)
            
    def btn_add_action(self):
        """Creates a object out of the PopUpWindow Class"""
        self.popup = PopUpWindow()
        self.popup.exec_()
        
    def btn_edit_action(self):
        """Creates a object out of the PopUpWindow Class 
        with the arugment that edit is True"""
        self.popup = PopUpWindow(edit=True)
        self.popup.exec_()
        
    def btn_remove_action(self):
        """Takes the value from the spinbox and depenting on which
        selectedFormat you have it removes an item from that list"""
        self.remove_value = self.spinbox.value()
        if selectedFormat == "Blueray":
            model.lista_BR.pop(int(self.remove_value)-1)
        elif selectedFormat == "DVD":
            model.lista_DVD.pop(int(self.remove_value)-1)
        elif selectedFormat == "VHS":
            model.lista_VHS.pop(int(self.remove_value)-1)
        
        self.clear_mainWindows()
        self.updateBR()
        self.updateDVD()
        self.updateVHS()
        model.set_saveBR()
        model.set_saveDVD()
        model.set_saveVHS()
  
        
    def run(self):
        """Starts the program"""
        self.show()
        sys.exit(app.exec_())
        
register = Register()

class PopUpWindow(QDialog):
    """A class that creates a popup window where you can add or edit a movie
    for the register."""
    def __init__(self, parent=None, edit=False):
        """Constructor of the PopUpWindow"""
        super(PopUpWindow, self).__init__(parent)
        self.setGeometry(300, 30, 700, 600)
        self.edit = edit
        self.dialogUI()
        self.setWindowTitle(selectedFormat)
        
        
    def dialogUI(self):
        """Here the GUI is created for the PopUpWindow"""
        
        #Creates a Gridlayout
        self.Dlayout = QGridLayout(self)
        self.Dlayout.setSpacing(10)
        
        #Creates all the QLabels and the LineEdits that belongs to them
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
        
        #If you wish to edit a movie the LineEdits will be filled with
        #the text of the movie you want to edit thanks to this.
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
        
        #Depending if you want to add or edit a movie different names have been given
        #to the button that applies the action.
        if self.edit == True:
            self.btnQDialog = QPushButton("Edit", self)
        else:
            self.btnQDialog = QPushButton("Add", self)  
        self.btnQDialog.clicked.connect(self.btnQDialog_action)
        
        #Adds all the widgets created to the layout
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
        """Controlls what the button of the window does, Add or Edit a movie"""
        
        #Takes the value from the LineEdits and saves them in new variables
        self.stringName = str(self.addNameText.text())
        self.stringGenre = str(self.addGenreText.text())
        self.stringDirector = str(self.addDirectorText.text())
        self.stringYear = str(self.addYearText.text())
        self.stringUnique = str(self.addUniqueText.text())
        
        #Creates an item based on the LineEdits values
        if self.edit == False:
            model.create_item(selectedFormat, self.stringUnique, self.stringName, \
            self.stringGenre, self.stringDirector, self.stringYear)
        
        #Edits an item based on the LineEdits values, the registers spinbox value
        #and selectedFormat
        elif self.edit == True:
            model.edit_item(selectedFormat, self.stringUnique, self.stringName, \
            self.stringGenre, self.stringDirector, self.stringYear, register.spinbox.value()-1)
            
        #Clears then runs the updates and the saves
        register.clear_mainWindows()
        register.updateBR()
        register.updateDVD()
        register.updateVHS()
        model.set_saveBR()
        model.set_saveDVD()
        model.set_saveVHS()
        
     
        
        

    
register.run()