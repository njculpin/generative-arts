import PIL, random, sys
from PIL import Image, ImageDraw
import numpy as np

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
    
def create_invader(border, draw, size):
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
      
def save_invader(size):
  origDimension = 512
  origImage = Image.new('RGBA', (origDimension, origDimension))
  draw = ImageDraw.Draw(origImage, 'RGBA')
  invaderSize = origDimension  
  padding = invaderSize/size
  for x in range(0, 1):
    for y in range(0, 1):
      topLeftX = x*invaderSize + padding/2
      topLeftY = y*invaderSize + padding/2
      botRightX = topLeftX + invaderSize - padding
      botRightY = topLeftY + invaderSize - padding
      create_invader((topLeftX, topLeftY, botRightX, botRightY), draw, size)
  return origImage
  

def sprite_invader(origImage, index):
  flat = origImage.copy()
  datas = flat.getdata()
  newData = []
  for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
      newData.append((255, 255, 255, 0))
    else:
      newData.append(item)
  flat.putdata(newData)  
  flat.save(str(index)+".png")     
      
def lighter(color, percent):
  color = np.array(color)
  white = np.array([255, 255, 255])
  vector = white-color
  return color + vector * percent

def darker(color, percent):
  color = np.array(color)
  black = np.array([0, 0, 0])
  vector = black-color
  return color + vector * percent


def main(size):
  for index in range(0,5):
    origImage = save_invader(size)
    sprite_invader(origImage, index)
  
  
  
if __name__ == "__main__":
  main(7)