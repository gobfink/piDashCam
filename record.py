import picamera
import datetime as dt
from numpy import inf

width = 1600
height = 900
frameRate = 24
fileName = '/media/pi/PNY-128G/timestamped.h264'
timeFormat = '%Y-%m-%d %H:%M:%S'
duration = inf
deltaFrame = 0.2
previewVideo = False


with picamera.PiCamera() as camera:
    camera.resolution = (width,height)
    camera.framerate = frameRate
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime(timeFormat)
    if previewVideo:
        camera.start_preview()
    camera.start_recording(fileName)
    start = dt.datetime.now()
    while (dt.datetime.now() - start).seconds < duration:
        camera.annotate_text = dt.datetime.now().strftime(timeFormat)
        camera.wait_recording(deltaFrame)
    camera.stop_recording()
