#=======================================================================
# Copyright (c) 2014  MicroTeknic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#=======================================================================

import pygame, os, sys, time
from pygame.locals import *

#variables
o = 1
global f
f = 1
main_dir = os.path.dirname(os.path.abspath(__file__))
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(main_dir, 'libs', 'music.mp3'))#load music
pygame.mixer.music.play(-1)

class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        myFont = pygame.font.SysFont("Calibri", 28)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False




def main():

    
    global f
    if f == 1:
        global screen
        screen = pygame.display.set_mode((800,600))
    elif f == 0:
        global screen
        screen = pygame.display.set_mode((800,600), FULLSCREEN)

    global score
    score = 0
    pygame.mouse.set_visible(1)
    #screen = pygame.display.set_mode((800,600))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))
    screen.blit(background, (0,0))
    pygame.display.set_caption("Sterioscopy Test Game")
    pygame.display.set_icon(pygame.image.load((os.path.join(main_dir, 'libs', 'MindSight.png'))))
    pygame.display.flip()
    #Setting up Background
    start_back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(start_back, (0, 0))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Sterioscopy Test Game!", 0, (255,0,0))
    screen.blit(title, (50, 100))
    #buttons
    StartButton = Button()
    QuitButton = Button()
    StartButton.create_button(screen, (107,142,35),230,180,300,100,0,"Start Game!", (255,255,255))
    QuitButton.create_button(screen, (225,0,0),230,300,300,100,0,"Quit Game", (255,255,0))
    
    pygame.display.flip()
    

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_f:
                if f == 1:
                    f = f-1
                elif f == 0:
                    f = f+1
                main()
            elif event.type == MOUSEBUTTONDOWN:
                    if StartButton.pressed(pygame.mouse.get_pos()):
                        Question1()
                    elif QuitButton.pressed(pygame.mouse.get_pos()):
                        pygame.quit()
    
def Question1():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    computer = pygame.image.load(os.path.join(main_dir, 'libs', 'computer.jpg'))
    screen.blit(computer, (0, 80))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 1", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Typewriter", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Computer", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Television", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Radio", (255,255,255))
    

    
    pygame.display.flip()
    
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question2()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question2()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question2()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        Question2()
                        
def Question2():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    car = pygame.image.load(os.path.join(main_dir, 'libs', 'car.gif'))
    screen.blit(car, (0, 80))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 2", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Car", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Boat", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Train", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Jet ski", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question3()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question3()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question3()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        Question3()

def Question3():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    pear = pygame.image.load(os.path.join(main_dir, 'libs', 'Pears.jpg'))
    screen.blit(pear, (10, 60))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 3", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Avacados", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Oranges", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Apples", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Pears", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question4()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question4()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question4()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question4()

def Question4():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    pear = pygame.image.load(os.path.join(main_dir, 'libs', 'train.jpg'))
    screen.blit(pear, (10, 60))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 4", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Grill", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Boat", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Train", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Power Plant", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question5()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question5()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question5()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        Question5()

def Question5():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    pear = pygame.image.load(os.path.join(main_dir, 'libs', 'hdd.jpg'))
    screen.blit(pear, (10, 60))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 5", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) CD", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Record", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Hard Drive", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Floppy Disk", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question6()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question6()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10  
                        Question6()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        Question6()

def Question6():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    computer = pygame.image.load(os.path.join(main_dir, 'libs', 'Potato.gif'))
    screen.blit(computer, (0, 80))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 6", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Rock", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Potato", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Dirt", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Radish", (255,255,255))
    

    
    pygame.display.flip()
    
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question7()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question7()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question7()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        Question7()
                        
def Question7():
    global screen,score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    car = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(car, (0, 80))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 2", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Car", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Boat", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Train", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Jet ski", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question8()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question8()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question8()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        Question8()

def Question8():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    pear = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(pear, (10, 60))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 3", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Avacados", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Oranges", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Apples", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Pears", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question9()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question9()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question9()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question9()

def Question9():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    pear = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(pear, (10, 60))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 3", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Avacados", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Oranges", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Apples", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Pears", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        Question10()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        Question10()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        Question10()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        Question10()

def Question10():
    global screen
    global score
    #Setting up Background
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    pear = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(pear, (10, 60))
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    #Render Title
    title = font.render("Question 3", 0, (255,0,0))
    screen.blit(title, (200, 20))
    title2 = font.render("What is", 0, (255,255,0))
    screen.blit(title2, (500, 140))
    title3 = font.render("this?", 0, (255,255,0))
    screen.blit(title3, (500, 180))
    #buttons
    ButtonA = Button()
    ButtonB = Button()
    ButtonC = Button()
    ButtonD = Button()
    ButtonA.create_button(screen, (0,0,255),10,400,180,80,0,"A) Avacados", (255,255,255))
    ButtonB.create_button(screen, (0,0,255),210,400,180,80,0,"B) Oranges", (255,255,255))
    ButtonC.create_button(screen, (0,0,255),410,400,180,80,0,"C) Apples", (255,255,255))
    ButtonD.create_button(screen, (0,0,255),610,400,180,80,0,"D) Pears", (255,255,255))
    

    
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if ButtonA.pressed(pygame.mouse.get_pos()):
                        End()
                    elif ButtonB.pressed(pygame.mouse.get_pos()):
                        End()
                    elif ButtonC.pressed(pygame.mouse.get_pos()):
                        End()
                    elif ButtonD.pressed(pygame.mouse.get_pos()):
                        correct = pygame.mixer.Sound(os.path.join(main_dir, 'libs', 'correct.wav'))  #load sound
                        correct.play()
                        score = score + 10
                        End()




def End():
    global screen
    global score
    back = pygame.image.load(os.path.join(main_dir, 'libs', 'background.jpg'))
    screen.blit(back, (0, 0))
    img = pygame.image.load(os.path.join(main_dir, 'libs', 'MindSight.png')).convert_alpha()
    screen.blit(img, (250, 50))
    scorepercent = 'Your score is ' + str(score) + '%'
    font = pygame.font.SysFont("monospace", 45)
    font.set_bold(True)
    grade = font.render(scorepercent, 0, (255,0,0))
    screen.blit(grade, (160, 20))
    pygame.display.update()
    pygame.display.flip()
    SaveButton = Button()
    QuitButton = Button()
    SaveButton.create_button(screen, (0,255,255),300,275,200,100,0,"Save Score!", (255,0,0))
    QuitButton.create_button(screen, (225,0,0),200,390,400,200,0,"Quit Game", (255,255,0))
    pygame.display.flip()
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                    if QuitButton.pressed(pygame.mouse.get_pos()):
                        pygame.quit()
                    elif SaveButton.pressed(pygame.mouse.get_pos()):
                        pygame.image.save(screen, (os.path.join(main_dir, 'Scores', 'Score' + str(score) + '.png')))
    
main()
    

                


    

