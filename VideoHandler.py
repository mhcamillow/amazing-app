from math import sqrt
import numpy as np
import cv2
from DrawBox import DrawBox

class VideoHandler:

  def create_box(self, width, heigth):
    self.box = DrawBox(width, heigth)

  def detect_eyes(self, frame):
    face_cascade = cv2.CascadeClassifier('C:/python/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:/python/haarcascade_eye.xml')
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

    eyes_return = {}
    for (x,y,w,h) in faces:
      roi_gray = gray_img[y:y+h, x:x+w]
      eyes = eye_cascade.detectMultiScale(roi_gray)

      for counter, (ex, ey, ew, eh) in enumerate(eyes):
        eyes_return[counter] = (x+ex, y+ey, ew, eh)

    return eyes_return

  def get_info_eyes(self, eyes):
    total_eyes = len(eyes)
    if total_eyes < 2: return 0

    reye = eyes[0]
    leye = eyes[1]
    center_r_eye = ((reye[0] + reye[0] + reye[2]) / 2, (reye[1] + reye[1] + reye[3]) / 2)
    center_l_eye = ((leye[0] + leye[0] + leye[2]) / 2, (leye[1] + leye[1] + leye[3]) / 2)
    
    center = ((center_r_eye[0] + center_l_eye[0]) / 2, (center_r_eye[1] + center_l_eye[1]) / 2)
    distance = sqrt(pow(center_r_eye[0] - center_l_eye[0], 2) + pow(center_r_eye[1] - center_l_eye[1], 2))

    return (center, distance)

  def teste(self, eyes):
    total_eyes = len(eyes)
    if total_eyes < 2: return 0

    return (eyes[0][0],eyes[0][1])

  def capture_video(self, input):
    cap = cv2.VideoCapture(input)
    first = True
    while(cap.isOpened()):
      ret, frame = cap.read()

      if first: 
        self.create_box(cap.get(3), cap.get(4))
        first = False
      print(frame)
      if frame != None:
        eyes = self.detect_eyes(frame)
        info = self.get_info_eyes(eyes)
      
        if info != 0:
          print(info[0])
          self.box.set_center(info[0])
          cv2.circle(frame,self.teste(eyes), 10, (0,0,255), -1)

        self.box.show_image()

        cv2.imshow('teste', frame)
      else:
        break

      if cv2.waitKey(15) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()

#x = VideoHandler()
#x.capture_video('sample.mp4')
#x.run()