import tkinter
from text_encryptor import texteditor
from pygame1 import cargame
from flappy_bird import flappybird
from clickspeed import click_speed_tester

#function to run the cargame
def runcargame():
   p = cargame()

#function to run the test encryptor
def text_encryptor():
   t = texteditor()

#function to run the click speed test 
def clickspeedtester():
   c = click_speed_tester()

#function to run the flappybird
def runflappybird():
   f = flappybird()

root = tkinter.Tk() #assigns root variable for tkinter
root.title("Ran's Family Arcade") #assigns title for the window 
root.geometry("1200x700") #assigns geometry for the window

#defines wilcoming instuctions
text = tkinter.Label(root, text="Welcome to Ran's Family Arcade!!! \n", font=('Times New Roman', 27,'bold')) #displays welcome message
instuctions = tkinter.Label(root, text=" Instrutions : There are 4 games in this arcade currently \n 1. the car game, in this game you will be driving a car on highway 420. \n There will be 2 enemy cars Pauxation and Deanation constantly coming in attempt to crash you. Be sure to dodge them！\n", font=('Times New Roman', 14,'bold'))
instuctions2 = tkinter.Label(root, text=" 2. Text encryptor, Do you ever wanna write something secret but don't know how? Ran's text encrypyor is here to help you!\n It is everything like a normal text editor, but you can encrypt and decrypt files \n", font=('Times New Roman', 14,'bold'))
instuctions3 = tkinter.Label(root, text="  3. click speed tester, click the grey pad as many times as you can in 5 seconds to see what your CPS is, \n if you want to go again after, click the restart button \n", font=('Times New Roman', 14,'bold'))
instuctions4 = tkinter.Label(root, text="  4. Flappy bird, this is a replica version of the popular game flappy bird \n but its way more easier so it won't make u want to smash your computer ^_^ \n", font=('Times New Roman', 14,'bold'))
#packs the welcome message onto the screen
text.pack() 
instuctions.pack()
instuctions2.pack()
instuctions3.pack()
instuctions4.pack()


#displays the 4 button to run the 4 different games
button_cargame = tkinter.Button(root, text ="Click here to play the car game", command = runcargame, pady = 10)
button_text = tkinter.Button(root, text ="Click here to start the text encryptor", command = text_encryptor, pady = 10)
button_clickspeed = tkinter.Button(root, text ="Click here to test you click speed", command = clickspeedtester, pady = 10)
button_flappybird = tkinter.Button(root, text ="Click here to play the flappybird", command = runflappybird, pady = 10)

#Packs the 4 buttons on the screen
button_cargame.pack()
button_text.pack()
button_clickspeed.pack()
button_flappybird.pack()

root.mainloop() #loops the window