from pygame_functions import *
import math, random, time, pickle



SCREEN_SIZE_W = 1800
SCREEN_SIZE_H = 1000

WORLD_SIZE = 10_000

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
        self.last_anim = clock()
        
        transformSprite(self.sprite, self.angle_deg,self.size/100)

    
    def add_images(self,images):
        for image in images:
            addSpriteImage(self.sprite,image)

    def move(self,player):
        
        now = clock()

        if now-self.last_anim<200:
            pass
        else:
            self.last_anim = now


        self.x = (self.x+self.velocity_x)%WORLD_SIZE
        self.y = (self.y+self.velocity_y)%WORLD_SIZE
        
        screen_max_x = player.x+SCREEN_SIZE_W//2
        screen_min_x = player.x-SCREEN_SIZE_W//2

        screen_max_y = player.y+SCREEN_SIZE_H//2
        screen_min_y = player.y-SCREEN_SIZE_H//2

        #print(f"x:{screen_max_x}, y:{screen_max_y}")
        
        
        
        screen_pos_x = (self.x-player.x)+SCREEN_SIZE_W//2
        screen_pos_y = (self.y-player.y)+SCREEN_SIZE_H//2

        showSprite(self.sprite)
        moveSprite(self.sprite,screen_pos_x,screen_pos_y,True)
        



class Player(Creature):

    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image, size)
        
        self.max_speed = 15
        self.alive = 1
        self.invulnerable = True
        self.invulnerability_period = 3000
        self.start = clock()
        print(self.start)
        moveSprite(self.sprite,SCREEN_SIZE_W//2,SCREEN_SIZE_H//2,True)
    
    def move(self,creatures):

         
        mouse_x = mouseX()
        mouse_y = mouseY()

        diff_x = mouse_x-SCREEN_SIZE_W//2
        diff_y = mouse_y-SCREEN_SIZE_H//2
        dist = math.sqrt(diff_x**2 + diff_y**2)
        self.speed = dist/200 * 10
        
        if self.invulnerable and clock()-self.start>=self.invulnerability_period:
            self.invulnerable = False
            
        
        
        
        if diff_x != 0:
            if diff_y !=0:
                self.angle_deg = math.degrees(math.atan2(diff_y,diff_x))
            else:
                self.angle_deg = 00 if diff_x>0 else 180
        else:
            self.angle_deg = 90 if diff_y>0 else -90
        

        
        self.velocity_x = math.cos(math.radians(self.angle_deg)) * self.speed
        self.velocity_y = math.sin(math.radians(self.angle_deg)) * self.speed
        
        
        transformSprite(self.sprite,self.angle_deg,self.size/100)
        #super().move(False)

        self.x=(self.x+self.velocity_x)%WORLD_SIZE
        self.y=(self.y+self.velocity_y)%WORLD_SIZE
        
        for c in creatures:
            if touching(self.sprite,c.sprite):
                if self.size>=c.size:
                    
                    creatures.remove(c)
                    self.size+=15
                    hideSprite(c.sprite)
                elif self.size<c.size and not self.invulnerable:

                    print("DEAD")
                    return False

        return True
def draw_boundary(player,fps,num):
    clearShapes()
    drawRect(SCREEN_SIZE_W//2-player.x,SCREEN_SIZE_H//2-player.y,WORLD_SIZE,WORLD_SIZE,(0,0,40),0)
    drawRect(SCREEN_SIZE_W//2-player.x,SCREEN_SIZE_H//2-player.y,WORLD_SIZE,WORLD_SIZE,(255,255,255),5)
    
    changeLabel(fps_label,f"FPS:{fps}")
    changeLabel(enemies_label,f"Enemies:{num}")
    showLabel(fps_label)
    showLabel(enemies_label)
    

setAutoUpdate(False)
enemies = []
for i in range(150):
    enemies.append(Creature(random.randint(0,WORLD_SIZE),random.randint(0,WORLD_SIZE), "Image_Files/sprite_0.png", random.randint(100,500)))
    enemies.append(Creature(random.randint(0,WORLD_SIZE),random.randint(0,WORLD_SIZE), "Image_Files/sprite_0.png", random.randint(1,100)))
    enemies[-1].add_images(["Image_Files/sprite_1.png","Image_Files/sprite_2.png","Image_Files/sprite_3.png"])

player = Player(WORLD_SIZE//2,WORLD_SIZE//2,"Image_Files/sprite_4.png",50)
FPS = 0

fps_label=makeLabel(f"FPS:{FPS}",50,0,0,fontColour="white")
enemies_label=makeLabel(f"Enemies:{len(enemies)}",50,0,50,fontColour="white")
showLabel(fps_label)

last = clock()
while True:

    for e in enemies:
        
        e.move(player)
    tick(24)
    time_taken=clock()-last
    
    last=clock()
    print(time_taken)
    draw_boundary(player,round(1/(time_taken/1000)),len(enemies))
    updateDisplay()
    if not player.move(enemies):
        break


        
endWait()
