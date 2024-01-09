import pip
import pygame
from pygame.locals import *
import random
from pygame import mixer

class flappybird:
   
    def __init__(self):

        pygame.init() #initilizes pygame
        mixer.init() #initilizes mixer to play music
        clock = pygame.time.Clock()
        fps = 60

        #sets screen dimensions and create the screen/title
        screen_width = 864
        screen_height = 936
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Rans Family Flappy Bird')

        font = pygame.font.SysFont('Bauhaus 93', 60) #font of the score

        ground_scroll = 0 #position of the ground
        scroll_speed = 4 #ground_scroll speed
        bird_height = 400 #height of the bird
        bird_falling_speed = -10 # initital velocity of the bird
        flying = False #defines flying variables so the bird won't start until user hits keyboard

        #load images
        bg = pygame.image.load('bg.png')
        ground_img = pygame.image.load('ground.png')

        pipe1_x = 880 # x position of the first pipe
        pipe2_x = 880 + int(screen_width/2) # x position of the second pipe
        pipe_y = random.choice([600, 400, 500])  # y position of the first pipe
        pipe2_y = random.choice([600, 400, 500]) # y position of the second pipe
        score = 0 #score of the user
        time_counter = 0 #variable to cont time, speed of pipe will increase as time goes  

        run = True #sets run variable, the program will run as long as this variable is true
        while run: #sets the loop
            clock.tick(fps) #sets frames rate
            self.screen.blit(bg, (0,0)) #displays the background

            #add 1 to the time counter, for every 800 it reaches, add 1 to the ground scrolling speed
            time_counter += 1 
            if time_counter % 800 == 0:
                scroll_speed += 1

            #physics setting for the bird and setting for the pipe, will run as long as the bird if flying
            if flying == True:
                bird_falling_speed += 0.5 
                if bird_falling_speed > 8: bird_falling_speed = 8
                bird_height += bird_falling_speed
                pipe1_x -= scroll_speed
                pipe2_x -= scroll_speed
                if pipe1_x < -50:
                    pipe1_x = 880
                    pipe_y = random.choice([600, 400, 500])
                if pipe2_x < -50: 
                    pipe2_x = 880
                    pipe2_y = random.choice([600, 400, 500])
            
            #displays pipes at previously defined position
            self.biltpipe(pipe1_x, pipe_y)
            self.biltpipe(pipe2_x, pipe2_y)


            img = pygame.image.load(f'bird{time_counter%3 + 1}.png') #load 3 different image each at a time to animate a wing affect
            self.screen.blit(img, (int(screen_width/4), bird_height)) #display it
            
            #check for collision, if so play endgame sound and set flying to false
            if int(screen_width/4) - 15 < pipe1_x < int(screen_width/4) + 10 and (pipe_y - 45 < bird_height or pipe_y - 185 > bird_height):
                flying = False
                scroll_speed = 0
                self.playmusic("crash.wav") 
                self.playmusic("gameover.mp3")
                break
            if int(screen_width/4) - 15 < pipe2_x < int(screen_width/4) + 10 and (pipe2_y - 45 < bird_height or pipe2_y - 185 > bird_height):
                flying = False
                scroll_speed = 0
                self.playmusic("crash.wav") 
                self.playmusic("gameover.mp3")
                break
            if bird_height > 750:
                flying = False
                scroll_speed = 0
                self.playmusic("crash.wav") 
                self.playmusic("gameover.mp3") 
                break


            #draw the ground
            self.screen.blit(ground_img, (ground_scroll, 768))
            #draw and scroll the ground
            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 35:
                ground_scroll = 0

            #run game forloop, check for jumping clicks or quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and flying == True:
                    bird_falling_speed = -10
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and flying == False:
                    flying = True

            
            #every time the pipe passes the bird, add 1 to the score and display the score
            if pipe1_x == 864 - scroll_speed * ((864-222) // scroll_speed) or pipe2_x == 864 - scroll_speed * ((864-222) // scroll_speed):
                score += 1
                print(score)
            self.draw_text(str(score), font, (255, 255, 255), int(screen_width / 2), 20)

            pygame.display.flip() #updates pygame screen
        
        

    #this function takes in the x and y coordinates of the top of the botton pipe, and displays it
    def biltpipe(self, x, y):
            pipe = pygame.image.load('pipe.png')
            self.screen.blit(pipe, (x, y))
            pipe2 = pygame.transform.flip(pipe, False, True)
            self.screen.blit(pipe2, (x, y-750))
    
    #this function displays text on the screen
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    #this function takes in audio file name and plays the song once
    def playmusic(self, filename):
        mixer.music.load(filename) #loads song
        mixer.music.set_volume(70) #sets volume to 70
        mixer.music.play() #plays song
        while pygame.mixer.music.get_busy(): #this while loop makes it so that the song will not end the moment after it starts 
            pygame.time.Clock().tick(1)
 
