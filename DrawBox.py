import numpy as np
import cv2

class DrawBox:

  def __init__(self, width, heigth):
    self.width =  int(width)
    self.heigth = int(heigth)
    self.sizeX = width / 2
    self.sizeY = heigth / 2
    self.lpressed = False
    self.rpressed = False
    self.centerX = 0
    self.centerY = 0
    cv2.namedWindow('potato')
    #cv2.setMouseCallback('potato', self.mouseEvents) -> Created to test some stuff
    self.img = np.zeros((self.heigth,self.width,3), np.uint8)

  def set_center(self, center):
    imgCenterX = self.width/2
    imgCenterY = self.heigth/2
    self.centerX = int(imgCenterX + (imgCenterX - center[0]))
    self.centerY = int(center[1])#imgCenterY + (imgCenterY - center[1]))

  def mouseEvents(self, event,x,y,flags,param):
    imgCenterX = self.width/2
    imgCenterY = self.heigth/2
    self.img[:] = (0,0,0)
    self.centerX = x#imgCenterX + (imgCenterX - x)
    self.centerY = y#imgCenterY + (imgCenterY - y)
    
    if event == cv2.EVENT_LBUTTONDOWN:
      self.lpressed = True
    elif event == cv2.EVENT_LBUTTONUP:
      self.lpressed = False

    if event == cv2.EVENT_RBUTTONDOWN:
      self.rpressed = True
    elif event == cv2.EVENT_RBUTTONUP:
      self.rpressed = False

  def draw(self):
    self.img[:] = (0,0,0)

    if self.lpressed:
      if self.sizeX <= self.width - 150:
        self.sizeX += (self.width  / 40)
        self.sizeY += (self.heigth / 40)

    if self.rpressed:
      if self.sizeY >= 40:
        self.sizeX -= (self.width  / 40)
        self.sizeY -= (self.heigth / 40)

    corner1 = (int(self.centerX - (self.sizeX/2)), int(self.centerY - (self.sizeY/2)))
    corner2 = (int(self.centerX + (self.sizeX/2)), int(self.centerY - (self.sizeY/2)))
    corner3 = (int(self.centerX - (self.sizeX/2)), int(self.centerY + (self.sizeY/2)))
    corner4 = (int(self.centerX + (self.sizeX/2)), int(self.centerY + (self.sizeY/2)))

    line1 = (0,0)
    line2 = (self.width, 0)
    line3 = (0, self.heigth)
    line4 = (self.width, self.heigth)

    cv2.rectangle(self.img, corner1, corner4, (0,255,0),  2)
    cv2.line(self.img, line1, corner1, (0,255,0), 2)
    cv2.line(self.img, line2, corner2, (0,255,0), 2)
    cv2.line(self.img, line3, corner3, (0,255,0), 2)
    cv2.line(self.img, line4, corner4, (0,255,0), 2)

  def show_image(self):
    self.draw()
    cv2.imshow('potato',self.img)

  def run(self):
    while(1):
      self.draw()
      cv2.imshow('potato',self.img)
      if cv2.waitKey(1) == 27:
        break

    cv2.destroyAllWindows()    

#x = DrawBox(800,600)
#x.run()