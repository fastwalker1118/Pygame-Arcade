#Author: Ran Qi
#Date Modified: May 19th 2022
#Description: Ran's car game

#imports all the prebuild codes that we need to use in our code
import pygame
import time
import random
from pygame import mixer

class cargame:

   def __init__(self):
      pygame.init() #initilizes pygame
      mixer.init() #initilizes mixer to play music

      fps = 60 #sets frame per second
      clock = pygame.time.Clock() #assign clock variable

      width = 800 #assigns width 
      height = 800 #assigns height
      grass = (60, 128, 0) #assigns grass color to green
      road = (50, 50, 50) #assigns the color of road
      yellow = (255, 240, 60) #creates yellow rgb for roadmark
      white = (255, 255, 255) #creates white rgb for roadmark
      self.screen = pygame.display.set_mode((width, height)) #assigns screen
      pygame.display.set_caption("Ran's Family car game") #Sets the caption that I want displayed at the top of the game window.

      mixer.music.load("bgm.mp3") #loads background music
      mixer.music.play(-1) # repeats on an infinite loop

      color_light = (215,100,0) # this is the light shade of the button for when user's mouse is not hovering over the button
      color_dark = (255,140,0) # this is the dark shade of the button for when user's mouse is hovering over the button
      r,g,b = 30, 0, 10 #sets rgb color and initilizes it to a number, this sets up for the background color change later in the gmae
      quagmire_x = 610 #sets the x-coordinate of quagmire image to 610, this sets up for the moving quagmire picture

      #The following code (line 49 to 84) sets the welcoming/instruction page before the actual game 
      instructionrunning = True #sets instruction as true
      while instructionrunning == True: #runs the forloop to display welcoming/instruction page as long as instructionrunning variable is true
         clock.tick(fps) #makes fps constant on each platform
         mouse = pygame.mouse.get_pos() #assigns the position of the users mouse to mouse variable  
         for event in pygame.event.get():        
            if event.type == pygame.QUIT: # Checks if the user click the window close button
                  pygame.quit() #if so, quit the program
            if event.type == pygame.MOUSEBUTTONDOWN: #Checks if a mouse is clicked     
                  #checks if the mouse is clicked on where the botton is
                  if width/8-5 <= mouse[0] <= width/2-width/8+220 and (height/2 + height/4) <= mouse[1] <= (height/2 + height/4)+40:
                     instructionrunning = False #if so, that means the user wants to move on, so we terminate the loop     
         r = r + 2 #plus 2 to R to change color
         g = g + 2 #plus 2 to g to change color
         b = b + 1 #plus 1 to B to change color
         if r >= 100:r=0 #if the value of red is great than 100, reset it to 0, I didn't choose 255 because it would make to color too bright
         if g >= 100:g=0 #if the value of green is great than 100, reset it to 0, I didn't choose 255 because it would make to color too bright
         if b >= 100:b=0 #if the value of blue is great than 100, reset it to 0, I didn't choose 255 because it would make to color too bright
         self.screen.fill((r,g,b)) #fill the screen with the current background color

         quagmire = pygame.image.load("quagmire.png") #uploads quamire image
         self.screen.blit(quagmire, (quagmire_x,500)) #displays it on screen with x coordinate being the one we previously set in line 49
         quagmire_x -= 3 #subtrct 3 from quagmire_x to make him move
         if quagmire_x < 530: quagmire_x = 610 #if its gets in the way of the button, we reset it to 610
         self.display(""" Welcome to Ran's Family Car game!!! """, 400, 80, (255, 255, 255), (r,g,b), 43) #first, we display welcoming message in yellow
         self.display("""Please use left/right arrow key to switch lanes""", 400, 180, (255, 255, 255), (r,g,b), 27) #displays the function of left/right arrow key
         self.display("""The car will automatically speed up as you go""", 400, 230, (255, 255, 255), (r,g,b), 27) #tells the user that the car will speed up as it goes
         self.display("""You can also press up arrow key to speed up""", 400, 280, (255, 255, 255), (r,g,b), 27) #displays the function of the up arrow key
         self.display("""You will also have 3 chances""", 400, 330, (255, 255, 255), (r,g,b), 27) #tells the user that he/she will have 3 chances to show down
         self.display("""to slow down by pressing the Down arrow key""", 400, 380, (255, 255, 255), (r,g,b), 27)#same message with the previous line, split to two lines so it fits into the screen
         self.display("""You can also use the WASD command to move""", 400, 430, (255, 255, 255), (r,g,b), 27)#same message with the previous line, split to two lines so it fits into the screen
            
         if width/8-50 <= mouse[0] <= width/2-width/8+220 and (height/2 + height/4) <= mouse[1] <= (height/2 + height/4)+40: # checks if user's mouse is hovering over the button
            pygame.draw.rect(self.screen,color_light,[width/8-50,(height/2 + height/4),480,40]) #if so, display the button in deeper color
         else: #if the users mouse if not on the button
            pygame.draw.rect(self.screen,color_dark,[width/8-50,(height/2 + height/4),480,40]) #if so, display the button in light color  
         # superimposing the text onto our button
         smallfont = pygame.font.SysFont('freesansbold.ttf',50) #sets font and size for the buttons
         text = smallfont.render("READY? Click to start!" , True , white) #sets the actual test and color
         self.screen.blit(text , (width/8 + 5, (height/2 + height/4 + 5)))  #displays the text and casts it on button
         pygame.display.flip() # updates the screen of the game so it constantly gets refrested

      road_w = int(width / 1.4) #assigns the with of the road in a relative scale to the actual width. cased to int to ensure we always end up with a whole number.

      #location parameters
      lane1 = int(width/2) - int(road_w/4) - int(road_w/8) #center of the first lane from left to right
      lane2 = int(width/2) - int(road_w/8) #center of the second lane from left to right
      lane3 = int(width/2) + int(road_w/8) #center of the third lane from left to right
      lane4 = int(width/2) + int(road_w/4) + int(road_w/8) #center of the fourth lane from left to right

      self.screen.fill(grass) #filles the screen with the background color green, kept out of the loop so it doesn't cover up anything else
      car = pygame.image.load("car.png") #load player vehicle
      car_loc = car.get_rect() #creates car_loc variable to get ready to display our car
      car_loc.center = lane1, height*0.8 #assigns the initial center of our car
      carspeed = [-int(road_w/4), 0] #creates carspeed variable and assigns it to how much it takes for car to switch 1 lane left
      carspeed2 = [int(road_w/4), 0] #creates carspeed2 variable and assigns it to how much it takes for car to switch 1 lane right
      self.screen.blit(car, car_loc) #display the car with the pre-assigned image and location

      car2 = pygame.image.load("otherCar.png") #loads enemy vehicle image
      car2_loc = car2.get_rect() #creates car2_loc variable to get ready to display the first enemy car
      car2_loc.center = lane3, height*0.2 #assigns the initial center of the first enemy car
      car2_loc2 = car2.get_rect() #creates car2_loc variable to get ready to display the second enemy car
      car2_loc2.center = lane2, height*0.2 #assigns the initial center of the second enemy car
      speed = 6 #creates the initial speed of enemy car 
      f = open("record.txt", "r") #this line reads an external text file containing the currect record socre of the user, it has to be an external file because if I assign record internally, it will get refershed every time the user runs the code
      record = int(f.read()) #reads the number in the file and cast it to an integer variable

      counter = 0 #creates counter variable, this variable will keep tract of users current score
      slowdowncount = 3 #creates slowdowncount variable, this variable will keep tract of how many chances the user has left to slow down

      running = True #creates running variable, the loop will keep going unless this variable is set to False inside the loop
      while running == True: #states a forloop to display the game until the running variable is set to False

         clock.tick(fps) #makes fps constant on each platform

         #The following 10 lines uses the display function to print current stats for the user, all of these states are displayed with text color yellow and background color green
         self.display("Score", 50, 40, (255, 250, 0), grass, 32) #displays the text "score" to show user the current score
         self.display(str(counter), 50, 80, (255, 250, 0), grass, 32) #the counter variable will be the current score, so display the counter variable
         self.display("Record", 745, 40, (255, 250, 0), grass, 32) #displays the text "Record" to show user the current record
         self.display(str(int(record)), 750, 80, (255, 250, 0), grass, 32) #the record variable will be the record, so we just print the record variable
         self.display("Speed", 745, 200, (255, 250, 0), grass, 32) #displays the text "Speed" to show user the current speed
         self.display(str(int(speed*10)) + "km/h", 748, 240, (255, 250, 0), grass, 25) #displays the speed to show user the current speed of enemy car
         self.display("Chances", 50, 200, (255, 250, 0), grass, 24) #displays test "Chances to Slow down" in three lines so its fits to the space availble
         self.display("to slow", 50, 230, (255, 250, 0), grass, 28) #scond line
         self.display("down", 50, 260, (255, 250, 0), grass, 28) #third line
         self.display(str(slowdowncount), 50, 300, (255, 250, 0), grass, 28) #displays how many chances the user has left

         counter += 1 #adds 1 to counter variable (the users score) every time the forloop runs
         if counter % 300 == 0: #checks if the user score is divisible by 300, this will be true every time the users score increase by 300
            speed += 0.5 #if so, adds 0.5 to speed
         for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # Checks if the user click the window close button
               pygame.quit() #if so, quit the program
            if event.type == pygame.KEYDOWN: #checks if the user is clicking a key
               if event.key == pygame.K_LEFT or event.key == pygame.K_a: #checks if the user is clicking the left arrow key
                  if car_loc.center[0] != lane1: #checks if the car is in the leftmost lane
                     car_loc = car_loc.move(carspeed) #if not, move the car by our pre-assigned carspeed variable so it moves 1 lane left
               # move user car to the right
               if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #checks if the user is clicking the right arrow key
                  if car_loc.center[0] != lane4: #checks if the car is in the rightmost lane
                     car_loc = car_loc.move(carspeed2) #if not, move the car by our pre-assigned carspeed variable so it moves 1 lane right
               if event.key == pygame.K_UP or event.key == pygame.K_w: #checks if the user is clicking the up arrow key
                  speed += 1 #if so, adds 1 to the speed of enemy car
               if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and slowdowncount > 0: #checks if the user is clicking the down arrow key and the user still have chance to slow down
                  speed -= 1 #if so, slows down by 1
                  slowdowncount -= 1 #minus 1 to slowdowncount

         #the following 7 lines draws the road and roadmarks on the screen
         roadmark_w = int(width/80) #assigns the width of roadmark
         pygame.draw.rect(self.screen, road ,[width/2 - road_w/2, 0, road_w, height]) #draws the main road
         pygame.draw.rect(self.screen, yellow ,[width/2 - roadmark_w/2, 0, roadmark_w, height]) #draws the leftmost yellow roadmark
         pygame.draw.rect(self.screen, yellow ,[width/2 - road_w/4 - roadmark_w/2, 0, roadmark_w, height]) #draws the middle yellow roadmark
         pygame.draw.rect(self.screen, yellow ,[width/2 + road_w/4 - roadmark_w/2, 0, roadmark_w, height]) #draws the rightmost yellow roadmark
         pygame.draw.rect(self.screen, white, [(width/2 - road_w/2 + roadmark_w*2 - 30), 0, roadmark_w, height]) #draws the white roadmark at the left of the road
         pygame.draw.rect(self.screen, white,[(width/2 + road_w/2 - roadmark_w*2 + 15), 0, roadmark_w, height]) #draws the white roadmark at the right of the road

         self.screen.blit(car, car_loc) #displays the image of our car with our pre-assigned locations
         self.screen.blit(car2, car2_loc) #displays the image of our first car with our pre-assigned locations
         self.screen.blit(car2, car2_loc2) #displays the image of our second enemy car with our pre-assigned locations

         car2_loc[1] += speed # moved the first enemy car down by the current speed variable
         car2_loc2[1] += speed # moved the second enemy car down by the current speed variable

         # what happens after the current enemy car gets out of our screen
         if car2_loc[1] > height: #if the current enemy cars are out of the screen
            if random.randint(0,1) == 0: #for the first enemy car, choose a random number between 0 and 1, check if its 0
                  car2_loc.center = lane3, -200 #if so, put first enemy car in lane 3
            else: 
                  car2_loc.center = lane4, -200 #if not, put first enemy car in lane 3
            if random.randint(0,1) == 0: #for the second enemy car, choose another random number between 0 and 1, check if its 0
                  car2_loc2.center = lane2, -200 #if so, put second enemy car in lane 2
            else: #Else (If 1) start in the left lane
                  car2_loc2.center = lane1, -200 #if not, put first enemy car in lane 1
                  
         # end game logic
         if (car_loc.center[0] == car2_loc.center[0] and car2_loc[1] >= car_loc[1] - 250) or (car_loc.center[0] == car2_loc2.center[0] and car2_loc2[1] >= car_loc [1] - 250): #checks for collusion
            if counter > record: #first we check to see if the score is bigger than record
               record = counter #if so, update local record variable to our score
               #the next 3 lines updates the record in the text file
               open('record.txt', 'w').close()
               with open("record.txt", "a") as f:
                  f.write(str(int(record)))
               self.display("Congrads, new record!", 400, 400, (255, 250, 0), (255, 0, 0), 64) #display breakrecord message on screen
               pygame.display.flip() #updates screen so user can see it
               self.playmusic("crash.wav") #plays collision sound
               self.playmusic("breakrecordsong.mp3") #plays song for breakrecord
            else:
               self.display("GAME OVER! YOU LOST!", 400, 400, (255, 250, 0), (255, 0, 0), 64) #display gameover message on screen
               pygame.display.flip() #updates screen so user can see it
               self.playmusic("crash.wav") #plays collision sound
               self.playmusic("gameover.mp3") #plays gameover soundeffect
            break #breaks the loop
      
         pygame.display.flip() #update the screen
   #this function takes in audio file name and plays the song once
   def playmusic(self, filename):
      mixer.music.load(filename) #loads song
      mixer.music.set_volume(70) #sets volume to 70
      mixer.music.play() #plays song
      while pygame.mixer.music.get_busy(): #this while loop makes it so that the song will not end the moment after it starts 
         pygame.time.Clock().tick(1)

   #this function takes in text, x coordinate, y coordinate, color, background coor and size as parameters and displays texts out based on these conditions
   def display(self, word, x, y, wordcolor, backgroundcolor, size):
      font = pygame.font.Font('freesansbold.ttf', int(size)) #sets font and size
      text = font.render(word, True, tuple(wordcolor), tuple(backgroundcolor)) #assigns text variable with input word, color, and background color
      textRect = text.get_rect() #creates textRect variable to get ready for display
      textRect.center = (int(x), int(y)) #sets center point as input states
      self.screen.blit(text, textRect) #display the text
