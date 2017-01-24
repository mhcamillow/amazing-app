from VideoHandler import VideoHandler
from DrawBox import DrawBox

class AmazingApp:

  def run(self):
    video = VideoHandler()
    video.capture_video('C:/python/sample.mp4')

x = AmazingApp()
x.run()    