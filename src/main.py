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
        
        self.velocity_x = random.uniform(-1,1)
        self.velocity_y = random.uniform(-1,1)
        while self.velocity_x==0:
            self.velocity_x = random.uniform(-1,1)
        while self.velocity_y==0:
            self.velocity_y = random.uniform(-1,1)
        
        self.angle_deg = math.degrees(math.atan2(self.velocity_y,self.velocity_x))
        
        transformSprite(self.sprite, self.angle_deg,self.size/100)

    
    def move(self):
        
        self.x = (self.x+self.velocity_x)%SCREEN_SIZE_W
        self.y = (self.y+self.velocity_y)%SCREEN_SIZE_H

        moveSprite(self.sprite,self.x,self.y,centre=True)

class Player(Creature):

    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image, size)
        
    
    def move(self):
        mouse_x = mouseX()
        mouse_y = mouseY()

        diff_x = mouse_x-self.x
        diff_y = mouse_y-self.y

        if diff_x != 0:
            if diff_y !=0:
                self.angle_deg = math.degrees(math.atan2(diff_y,diff_x))
            else:
                self.angle_deg = 00 if diff_x>0 else 180
        else:
            self.angle_deg = 90 if diff_y>0 else -90
        
        
            

        


        transformSprite(self.sprite,self.angle_deg,self.size/100)




setAutoUpdate(False)
enemies = []
for i in range(30):
    enemies.append(Creature(random.randint(0,SCREEN_SIZE_W),random.randint(0,SCREEN_SIZE_H), "Image_Files/sprite_0.png", random.randint(10,100)))

player = Player(900,500,"Image_Files/sprite_4.png",100)

while True:
    for e in enemies:
        e.move()
    tick(30)
    updateDisplay()
    player.move()


        
endWait()
