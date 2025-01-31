from pygame_functions import *
import math, random, time, pickle



SCREEN_SIZE_W = 1800
SCREEN_SIZE_H = 1000

screenSize(SCREEN_SIZE_W,SCREEN_SIZE_H)
setBackgroundColour("black")

class Character:

    def __init__(self,x,y,image,size):

        self.x = x
        self.y = y
        self.size = size
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, 0, self.size/100)
        showSprite(self.sprite)

class Creature(Character):
    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image,size)
        
        self.speed = random.uniform(1,0)
        self.angle_deg = random.randint(0,360)
        
        
        transformSprite(self.sprite, self.angle_deg,self.size/100)

    
    def move(self):
        
        self.x = ((math.cos(math.radians(self.angle_deg))*self.speed)+self.x)%SCREEN_SIZE_W
        self.y = ((math.sin(math.radians(self.angle_deg))*self.speed)+self.y)%SCREEN_SIZE_H

        moveSprite(self.sprite,self.x,self.y,centre=True)

class Player(Creature):

    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image, size)
    
    def move(self):
        mouse_x = mouseX()
        mouse_y = mouseY()

        diff_x = mouse_x-self.x
        diff_y = mouse_y-self.y

        self.angle_deg = math.degrees(math.atan(diff_y/diff_x))


        transformSprite(self.sprite,self.angle_deg,self.size)




setAutoUpdate(False)
enemies = []
for i in range(30):
    enemies.append(Creature(random.randint(0,SCREEN_SIZE_W),random.randint(0,SCREEN_SIZE_H), "Image_Files/sprite_0.png", random.randint(10,100)))

player = Player(500,900,"Image_Files/sprite_4.png",100)

while True:
    for e in enemies:
        e.move()
    tick(30)
    updateDisplay()
    player.move()


        
endWait()
