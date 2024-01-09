# Importing Required libraries & Modules
from ctypes import sizeof
import this
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import string

class texteditor:

    def __init__(self):
        #the list below assigns each letter to a corresponding encrypted code, builds the base for the encrypyion program later
        self.thisdict = {
        "a": "@#$**",
        "b": "$*(@*",
        "c": "(*&^*",
        "d": "^&*$*",
        "e": "*#^&*",
        "f": "!@#$*",
        "g": "!#$^*",
        "h": "!&*(*",
        "i": "@%^^*",
        "j": "tZLOP",
        "k": "7VRjm",
        "l": "YiFVB",
        "m": "uS7np",
        "n": "2U6kH",
        "o": "iJajP",
        "p": "VFLse",
        "q": "7kTsO",
        "r": "hBNDE",
        "s": "juqHz",
        "t": "BncF3",
        "u": "fHhkD",
        "v": "ID1FE",
        "w": "5vToi",
        "x": "3fU0W",
        "y": "xW5ty",
        "z": "hvnCd",
        }
        #the code above only assigns code for lower case letters, line 43 to 54 assigns code for upper case letters and some common sysbols
        for c in string.ascii_uppercase :
            a = self.thisdict[c.lower()] 
            s = list(a)
            s[0] = ')'
            self.thisdict[c] = "".join(s)
        self.thisdict[" "] = "JKLMN"
        self.thisdict[","] = "SKCID"
        self.thisdict["."] = "KCUFF"
        self.thisdict["?"] = "HCTIB"
        self.thisdict["!"] = "CHILL"
        self.thisdict["\n"] = "CHIKL"
        self.thisdict[";"] = "SMART"
        
        root = Tk() #assigns roots variable for tkinter
        root.title("Ran's text editor") #assigns title for the window
        root.geometry("1200x700") #assigns geometry for the window

        frame = Frame(root) #assigns frame
        frame.pack(pady = 10) #assigns pady for the frame

        self.text = Text(frame, width = 100, height = 100)#assigns text area
        self.text.pack() #packs it onto the screen

        #makes a menu on the wondow
        my_menu = Menu(root) 
        root.config(menu = my_menu)

        file_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label="File", menu = file_menu) #adds file option for the menu
        file_menu.add_command(label="Open", command = self.openfile) #adds a option to open file when user clicks on file
        file_menu.add_command(label="Save As", command = self.saveas) #adds a option to save file when user clicks on file
        
        file_menu2 = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label="Encryption", menu = file_menu2) #adds encryption option for the menu
        file_menu2.add_command(label="Encrypted file and save", command = self.saveencrypt) #option to save the current file as encrypted file

        file_menu2 = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label="Decryption", menu = file_menu2) #adds decryption option for the menu
        file_menu2.add_command(label="Open an encrypted file", command = self.decrypt) #optio to open an encrypted file and open it as normal letters

        root.mainloop() #loop the window

    #this function is the logic for decryption
    def decrypt(self):
        self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        infile = open(self.filename,"r")
        str = infile
        combo = []
        for cha in infile:
            for line in cha:
                combo.append(line)
                if len(combo) == 5:
                    str = "".join(combo)
                    combo.clear()
                    self.key_list = list(self.thisdict.keys())
                    self.val_list = list(self.thisdict.values())
                    letter = self.key_list[self.val_list.index(str)]
                    self.text.insert(END,letter)
        infile.close()

    #this function is the logic for encryption
    def saveencrypt(self):
        file = filedialog.asksaveasfilename(title = "Save file As", defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        ourfile = self.text.get("1.0",END)
        outfile = open(file,"w")
        for line in ourfile:
            outfile.write(self.thisdict[line])
        outfile.close()
        outfile.write(file)

    #this function is the logic for save file
    def saveas(self):
        file = filedialog.asksaveasfilename(title = "Save file As", defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        ourfile = self.text.get("1.0",END)
        outfile = open(file,"w")
        outfile.write(ourfile)
        outfile.close()
        self.text.delete("1.0", END)
        file = self.text.get("1.0",END)
        outfile.write(file)

    #this function is the logic to open a file from computer
    def openfile(self):
        self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        infile = open(self.filename,"r")
        self.text.delete("1.0", END)
        for line in infile:
          self.text.insert(END,line)
        infile.close()

