# GENERATIVE SPACE BATTLES
# Nick Culpin

# DRAW SPRITES
import PIL, random, sys
from PIL import Image, ImageDraw
import numpy as np

screenSize = 600
r = lambda: random.randint(25,230)
rc = lambda: (r(), r(), r())
listSym = []

def create_square(border, draw, randColor, element, size):
  if (element == int(size/2)):
    draw.rectangle(border, randColor)
  elif (len(listSym) == element+1):
    draw.rectangle(border,listSym.pop())
  else:
    listSym.append(randColor)
    draw.rectangle(border, randColor)
    
def create_ship(border, draw, size):
  x0, y0, x1, y1 = border
  squareSize = (x1-x0)/size
  randColors = [rc(), rc(), rc(), (0,0,0), (0,0,0), (0,0,0)]
  i = 1
  for y in range(0, size):
    i *= -1
    element = 0
    for x in range(0, size):
      topLeftX = x*squareSize + x0
      topLeftY = y*squareSize + y0
      botRightX = topLeftX + squareSize
      botRightY = topLeftY + squareSize
      randomColor = random.choice(randColors)
      create_square((topLeftX, topLeftY, botRightX, botRightY), draw, randomColor, element, size)
      if (element == int(size/2) or element == 0):
        i *= -1;
      element += i
      
def draw_ship():
  origDimension = 512
  origImage = Image.new('RGBA', (origDimension, origDimension))
  draw = ImageDraw.Draw(origImage, 'RGBA')
  shipSize = origDimension  
  padding = shipSize/7
  for x in range(0, 1):
    for y in range(0, 1):
      topLeftX = x*shipSize + padding/2
      topLeftY = y*shipSize + padding/2
      botRightX = topLeftX + shipSize - padding
      botRightY = topLeftY + shipSize - padding
      create_ship((topLeftX, topLeftY, botRightX, botRightY), draw, 7)
  sprite = origImage.copy()
  datas = sprite.getdata()
  newData = []
  for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
      newData.append((255, 255, 255, 0))
    else:
      newData.append(item)
  sprite.putdata(newData)
  maxsize = (32, 32)
  sprite.thumbnail(maxsize, Image.ANTIALIAS)  
  return sprite


def darker(color, percent):
  color = np.array(color)
  black = np.array([0, 0, 0])
  vector = black-color
  return color + vector * percent


# GAME LOGIC
import pygame, sys
from pygame.locals import *

class Hero(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        
        ship_sprite = draw_ship()
        mode = ship_sprite.mode
        size = ship_sprite.size
        data = ship_sprite.tobytes()
        
        self.ship = pygame.image.fromstring(data, size, mode)         
        self.surf = pygame.Surface((50, 80))
        
        randomLeft = (0, random.randint(50, 550))
        randomTop = (random.randint(50, 550), 0)
        randomBottom = (random.randint(0, 550), 600)
        randomRight = (600, random.randint(50, 550))
        randomSpawn = random.choice([randomLeft, randomRight, randomTop, randomBottom])        
        self.rect = self.surf.get_rect(center = (randomSpawn))
        
        self.reset_offset = 0
        self.offset_x = random.randrange(-30, 30)
        self.offset_y = random.randrange(-30, 30)
        
        if self.reset_offset == 0:
          self.offset_x = random.randrange(-30, 30)
          self.offset_y = random.randrange(-30, 30)
          self.reset_offset = random.randrange(120, 150)
        else:
          self.reset_offset -= 1         
        
      def move(self):
        
        if E1.rect.x + self.offset_x > self.rect.x:
          self.rect.x += 1
        elif E1.rect.x + self.offset_x < self.rect.x:
          self.rect.x -= 1
      
        if E1.rect.y + self.offset_y > self.rect.y:
          self.rect.y += 1
        elif E1.rect.y + self.offset_y < self.rect.y:
          self.rect.y -= 1
 
      def draw(self, surface):
        surface.blit(self.ship, self.rect)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        
        ship_sprite = draw_ship()
        mode = ship_sprite.mode
        size = ship_sprite.size
        data = ship_sprite.tobytes()
        
        self.ship = pygame.image.fromstring(data, size, mode)         
        self.surf = pygame.Surface((50, 80))
        
        randomLeft = (0, random.randint(50, 550))
        randomTop = (random.randint(50, 550), 0)
        randomBottom = (random.randint(0, 550), 600)
        randomRight = (600, random.randint(50, 550))
        randomSpawn = random.choice([randomLeft, randomRight, randomTop, randomBottom])        
        self.rect = self.surf.get_rect(center = (randomSpawn))
        
        self.reset_offset = 0
        self.offset_x = random.randrange(-30, 30)
        self.offset_y = random.randrange(-30, 30)
        
        if self.reset_offset == 0:
          self.offset_x = random.randrange(-30, 30)
          self.offset_y = random.randrange(-30, 30)
          self.reset_offset = random.randrange(120, 150)
        else:
          self.reset_offset -= 1        
 
      def move(self):
                
        if HERO.rect.x + self.offset_x > self.rect.x:
          self.rect.x += 1
        elif HERO.rect.x + self.offset_x < self.rect.x:
          self.rect.x -= 1
      
        if HERO.rect.y + self.offset_y > self.rect.y:
          self.rect.y += 1
        elif HERO.rect.y + self.offset_y < self.rect.y:
          self.rect.y -= 1        
 
      def draw(self, surface):
        surface.blit(self.ship, self.rect)

HERO = Hero()      
E1 = Enemy()

def main():
  pygame.init()
  
  screen = pygame.display.set_mode([600, 600])
  
  FPS = 60
  FramePerSec = pygame.time.Clock()
    
  while True:     
    for event in pygame.event.get():              
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    E1.move()
    HERO.move()
  
    screen.fill((0, 0, 0))
    
    E1.draw(screen)
    HERO.draw(screen)
  
    pygame.display.update()
    FramePerSec.tick(FPS)
  
  
if __name__ == "__main__":
  main()