from pygame_functions import *
import math, random, time, pickle

screenSize(1000,1000)
setBackgroundColour("black")

SCRREN_SIZE = 100

class Character:

    def __init__(self,x,y,image,size):

        self._x = x
        self._y = y
        self._size = size
        self._sprite = makeSprite(image)
        moveSprite(self._sprite,self._x,self._y,centre=True)
        transformSprite(self._sprite, 0, self._size/100)
        showSprite(self._sprite)
class Creature(Character):
    def __init__(self,x,y,image,  size):
        super().__init__(x,y,image,size)
        
        self.x_speed = 0
        self.y_speed = 0

        




setAutoUpdate(False)
for i in range(40):
    c1 = Creature(random.randint(0,1000),random.randint(0,1000), "Image_Files/sprite_0.png", random.randint(100,400)) 

updateDisplay()
        
endWait()
