import pygame
import time
from pygame1 import cargame

class click_speed_tester:

    def __init__(self):

        pygame.init() #initilizes pygame
        instructionrunning = True #sets instruction as true

        fps = 60
        clock = pygame.time.Clock()

        width = 800 #assigns width 
        height = 800 #assigns height
        self.screen = pygame.display.set_mode((width, height)) #assigns screen
        color_light = (211, 211, 211) #color of the pad when the users mouse isn't hovering over it
        color_dark = (188, 188, 188) #color of the pad when the users mouse is hovering over it
        self.screen.fill((255, 255, 255)) #makes the background color of the screen white
        count = 0 #definds count variable, counts how many timer the user clicks
        run_timer = 0 #timer, used to give the user a time limir of 5 seconds
        run_times = 0 #this variable is used to keep track of if the user have finished a trail, will be resetted to 0 if the user clicks on the restart button
        start_ticks=pygame.time.get_ticks() #starter tick

        while instructionrunning == True:   
            clock.tick(fps)

            #the following 3 lines display welcoming message and inofrmation for user
            self.display("Welcome to Ran's Family Click Speed Tester", 400, 50, (0, 0, 0), (255, 255, 255), 28) #third line
            self.display("Did you know - clock speed is a very important factor in almost all vidoe games", 400, 150, (0, 0, 0), (255, 255, 255), 18) #third line
            self.display("Ever wondered how fast you click? Well, test it out here!", 400, 185, (0, 0, 0), (255, 255, 255), 18) #third line
            
            self.display(" Your Score : " + str(count) + "  ", 400, 400, (0, 0, 0), (255, 255, 255), 28 )#displays the score of user

            mouse = pygame.mouse.get_pos() #gets where the users mouse is
            for event in pygame.event.get():        
                if event.type == pygame.QUIT: # Checks if the user click the window close button
                    pygame.quit() #if so, quit the program
                
                #checks if the user clicks on the pad, if so, add 1 to count variable and make running ture and draw pad in color dark
                if event.type == pygame.MOUSEBUTTONDOWN and width/2-250 <= mouse[0] <= width/2+250 and height/2 + 50 <= mouse[1] <= height/2 + 300 and run_times == 0: #Checks if a mouse is clicked                    
                    count+=1
                    run_timer = 1
                    pygame.draw.rect(self.screen,color_dark,[width/2-250,height/2+50,500,250])

                #checks if the user click on restart button, if so, reset the game
                elif event.type == pygame.MOUSEBUTTONDOWN and width/2- 100 <= mouse[0] <= width/2 + 120 and height/2 - 110 <= mouse[1] <= height/2 - 30 and run_times == 1: #Checks if a mouse is clicked                    
                    run_times = 0
                    count = 0
                    run_timer = 0
                    start_ticks=pygame.time.get_ticks()
                #if nothing happens, draw the pad in light color
                else:
                    pygame.draw.rect(self.screen,color_light,[width/2-250,height/2+50,500,250])


            if run_timer == 1:
                seconds= int((pygame.time.get_ticks()-start_ticks)/100) / 10 #calculate how many seconds
                if seconds>=5: # if more than 10 seconds close the game
                    run_timer = 0
                    run_times += 1
                self.display(" " + str(seconds) + " ", 400, 350, (0, 0, 0), (255, 255, 255), 28) #print how many seconds
            else:
                self.display("0.0", 400, 350, (0, 0, 0), (255, 255, 255), 28) #print how many seconds

            if run_times == 1:
                if width/2- 100 <= mouse[0] <= width/2 + 120 and height/2 - 110 <= mouse[1] <= height/2 - 30: # checks if user's mouse is hovering over the button
                    pygame.draw.rect(self.screen,color_dark,[width/2 - 100 ,height/2 - 110,220,30]) #if so, display the button in deeper color
                else: #if the users mouse if not on the button
                    pygame.draw.rect(self.screen,color_light,[width/2 - 100 ,height/2 - 110,220,30]) 
                smallfont = pygame.font.SysFont('freesansbold.ttf',30) #sets font and size for the buttons
                text = smallfont.render("Click here to restart" , True , (0, 0, 0)) #sets the actual test and color
                self.screen.blit(text , (width/2 - 90, (height/2  - 110)))  #displays the text and casts it on button
                self.display(" Your CPS : " + str(count / 5), 400, 750, (0, 0, 0), (255, 255, 255), 28) #print click per second
            else:
                self.display(" Your CPS : 0.0 ", 400, 750, (0, 0, 0), (255, 255, 255), 28) #if the user havent started, print "you cps : 0"
            
            pygame.display.flip()

     
            
    #this function takes in text, x coordinate, y coordinate, color, background coor and size as parameters and displays texts out based on these conditions
    def display(self, word, x, y, wordcolor, backgroundcolor, size):
      font = pygame.font.Font('freesansbold.ttf', int(size)) #sets font and size
      text = font.render(word, True, tuple(wordcolor), tuple(backgroundcolor)) #assigns text variable with input word, color, and background color
      textRect = text.get_rect() #creates textRect variable to get ready for display
      textRect.center = (int(x), int(y)) #sets center point as input states
      self.screen.blit(text, textRect) #display the text




