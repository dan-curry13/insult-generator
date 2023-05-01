import random
import sys, os
from PyQt5.QtWidgets import QApplication, QMessageBox, QRadioButton, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

basedir = os.path.dirname(__file__)

CUST_NAME_MAX_LEN = 24
TOTAL_COLUMNS = 6

insultDictionary = {
    "pre_descriptor": ["Young ","Big ","Grand ","Lil' ","Old ","Scrunty ","Little "
                        "Bitchass ","Friggin' ","Sweaty ","Shitty "],
    "title": ["Chief ","Sergeant ","Corporal ","Major ","Private ","Captain ","Sir ",
                "Doctor ","Professor ","Archbishop ","Baron ","King ","Chairman ",
                "Chancellor ","Colonel ","Duke ","Emperor ","Inquisitor ","Mayor ",
                "Lord ","Monsignor ","Count ","Officer ","Grandmaster ","Ambassador ",
                "Monsieur ","Saint "],
    "title_no_predsc": ["His Holiness ","His Eminence ","The Honorable ","Big Ol' ",
                        "Super Chieftain ","The Dishonorable "],
    "name": ["Franky ","Bobby ", "Tony ","Donny ","Billy ","Freddy ","Jerry ","Charlie ",
                "Mikey ","Ricky ","Tommy ","Vinny ","Joey ","Robby ","Sammy ","Teddy ",
                "Jamie ","Rocky ","Reggie ","Howie ","Perry ","Monty ","Timmy ","Jimmy ",
                "Johnny ","Rudy ","Sully ","Wally ","Andy ","Bertie "],
    "name_custom": [""],           
    "prefix": ["Mc","Mac","O'","Van ","Von ","Le'","La","De"],
    "insult": ["Cunt","Fuck","Bitch","Shitt","Twatt","Dick","Cock","Scrunt","Bunt",
                "Taint","Doink","Ass","Frigg","Piss","Nutt","Cuck","Grund","Chod",
                "Gooch","Scrot","Boof","Scrumb","Jizz","Dong"],
    "insult_no_postfix" : ["Cunt","Fuck","Bitch","Shit","Twat","Dick","Cock","Scrunt","Bunt",
                "Taint","Doink","Piss","Nut","Cuck","Grundy","Chode","Puss","Beef","Meat",
                "Gooch","Scrot","Boof","Jizz","Dong"],
    "insult_standalone": ["Cocktopus","Dingus","Drangus","Dingo","Ringo","Rango",
                            "Rangus","Ringus","Brazzers","Bangbus","Bongos","Tittyboy",
                            "Krombobulous"],
    "postfix": ["le","ing","er","o"],
    "flair": ["house","stein","son","ton","man","cock","dick","rod","burn","by","tron",
                "nips","tits","cunt","skin","bus","bitch","mouth","miser","bag","sack",
                "ham","boy","master","bus","land","tuck","hub","way","cottage","sticks",
                "knees","milk","buckets","worth","sworth","sway","shaft","puss"],
    "flair_no_postfix": ["ioli","erino","ington","olious","-O","asaurus","alonious",
                        "-o-rama","let","nipples","shaft","meister","packer","tent"],
    "post_descriptor": [" Supreme"," Prime"," Eternal"," Superior",", Esquire",", PhD",
                        " III"," IV",", MD"," Unbounded"," Unlimited"," Everlasting",
                        " Unending"," Jr."," Sr."," Maximus"]
}

prefixTemplates = [
    ["pre_descriptor","name"],
    ["title_no_predsc","name"],
    ["title","name"],
    ["name"],
    ["pre_descriptor","name_custom"],
    ["title_no_predsc","name_custom"],
    ["title","name_custom"],
    ["name_custom"],
    ["pre_descriptor","title"],
    ["title_no_predsc"],
    ["title"],
    ["pre_descriptor"]
]

insultTemplates = [
    ["insult","postfix","flair"],
    ["insult","flair_no_postfix"],
    ["insult_standalone"],
    ["insult_no_postfix","flair"],
    ["prefix","insult","postfix","flair"],
    ["prefix","insult","flair_no_postfix"],
    ["prefix","insult_standalone"],
    ["prefix","insult_no_postfix","flair"]
]

postfixTemplate = [
    ["post_descriptor"]
]  

winNames = ["Devastating!","Diabolical!","Destroyed!","Roasted!","Burn!","Gottem!","Ha!",
            "Damaging!",":(","Ruinous!","Catastrophic!","Brutal!","Crippling!",
            "Lampooned!","Sheesh!","Bitch!"]

class RandStringGen:
    def __init__(self):
        self.genstring = ""
        self.temp = []

    def clear(self):
        self.genstring = ""
        self.temp = []

    def add(self, component):
        self.genstring += random.choice(component)
    
    def template(self, *templates):
        for t in templates:
            self.temp += random.choice(t)
            
    def generate(self,dictionary):
        for element in self.temp:
            self.add(dictionary[element])

class Insulter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Insulter v420.69")
        self.setObjectName("MainWindow")
        self.setGeometry(100, 100, 640, 600)        

        # Insult object
        self.insult = RandStringGen()

        # Create a central widget and layout
        self.central_widget = QWidget()
        self.layout = QGridLayout()

        # Background
        stylesheet = '''
            #MainWindow {
                background-image: url(data/laughing.jpg);
                background-repeat: repeat;
                background-position: center;
            }
        '''        
        self.setStyleSheet(stylesheet)

        # Header labels
        self.header = QLabel("What's up you big piece of shit!", self.central_widget)
        self.header.setStyleSheet("font-size: 30pt; color: white;")
        self.layout.addWidget(self.header, 0,0,1,TOTAL_COLUMNS, Qt.AlignCenter)
        self.label = QLabel("How may I insult you today?", self.central_widget)
        self.label.setStyleSheet("font-size: 24pt; color: white;")
        self.layout.addWidget(self.label, 1,0,1,TOTAL_COLUMNS, Qt.AlignCenter)

        # Checkbox options
        self.use_name = QLabel("Use Name: ", self.central_widget)
        self.rand_name = QRadioButton("Random", self.central_widget)
        self.cust_name = QRadioButton("Entered", self.central_widget)
        self.no_name = QRadioButton("None", self.central_widget)
        self.use_name.setStyleSheet("font-size: 18pt; color: white;")
        self.rand_name.setStyleSheet("font-size: 18pt; color: white;")
        self.cust_name.setStyleSheet("font-size: 18pt; color: white;")
        self.no_name.setStyleSheet("font-size: 18pt; color: white;")
        self.no_name.setChecked(True)
        self.layout.addWidget(self.use_name, 2,1, Qt.AlignRight)
        self.layout.addWidget(self.rand_name, 2,2)
        self.layout.addWidget(self.cust_name, 2,3)
        self.layout.addWidget(self.no_name, 2,4)

        # User name entry
        self.name_entry = QLineEdit("What's your name bitch?", self.central_widget)
        self.name_entry.setFixedWidth(220)
        self.name_entry.setStyleSheet("font-size: 14pt;")
        self.name_entry.setMaxLength(CUST_NAME_MAX_LEN)
        self.layout.addWidget(self.name_entry, 3,0,1,TOTAL_COLUMNS, Qt.AlignCenter)

        # Submit button
        self.submit_btn = QPushButton("Insult me!", self.central_widget)
        self.submit_btn.setStyleSheet("font-size: 18pt;")
        self.submit_btn.clicked.connect(self.assembleInsult)
        self.layout.addWidget(self.submit_btn, 4,0,1,TOTAL_COLUMNS, Qt.AlignCenter)

        # Set the layout on the central widget
        self.central_widget.setLayout(self.layout)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

    # Get custom name
    def submit_text(self):
        # Get text from text field
        text = self.name_entry.text()

        # Check if text is only letters and length is <= CUST_NAME_MAX_LEN
        if text.isalpha() and len(text) <= CUST_NAME_MAX_LEN:
            insultDictionary["name_custom"][0] = text + " "
            self.text_read_error = False
        # Otherwise show error message
        else:
            error_win = QMessageBox()
            error_win.setWindowTitle("What an idiot!")
            error_win.setText("Text entry is A-Z chars only, " + str(CUST_NAME_MAX_LEN) + " chars max. Dumbass!")
            error_win.exec()
            self.text_read_error = True

    def assembleInsult(self):
        self.insult.clear()
        # which checkbox
        if self.rand_name.isChecked():
            self.insult.template(prefixTemplates[0:3],insultTemplates)
        elif self.cust_name.isChecked():
            self.submit_text()
            if self.text_read_error:
                return
            self.insult.template(prefixTemplates[4:7],insultTemplates)
        else:
            self.insult.template(prefixTemplates[8:],insultTemplates)
        if len( self.insult.temp) <= 3:
            self.insult.template(postfixTemplate)
        self.insult.generate(insultDictionary) 
        severe_burn = QMessageBox()
        severe_burn.setWindowIcon(QIcon(os.path.join(basedir,'data\icon.ico')))
        severe_burn.setWindowTitle(random.choice(winNames))
        severe_burn.setText(self.insult.genstring)
        severe_burn.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir,"data\icon.ico")))
    viewer = Insulter()
    viewer.show()
    sys.exit(app.exec_())