import picamera
import datetime as dt
from numpy import inf

width = 1600
height = 900
frameRate = 24
filePath = '/media/pi/PNY-128G/'
fileNameFormat = '%Y-%m-%d:%H.h264'
timeFormat = '%Y-%m-%d %H:%M:%S'
duration = inf
delta_record = 0.2
previewVideo = False


with picamera.PiCamera() as camera:
    camera.resolution = (width,height)
    camera.framerate = frameRate
    camera.annotate_background = picamera.Color('black')
    current_time = dt.datetime.now()
    camera.annotate_text = current_time.strftime(timeFormat)
    if previewVideo:
        camera.start_preview()
    fileName = current_time.strftime(fileNameFormat)
    complete_path = filePath + fileName
    camera.start_recording(complete_path)
    start = dt.datetime.now()
    past_hour=dt.datetime.now().hour
    while (dt.datetime.now() - start).seconds < duration:
        if past_hour != dt.datetime.now().hour:
            current_time = dt.datetime.now()
            fileName = current_time.strftime(fileNameFormat)
            complete_path = filePath + fileName
            camera.split_recording(complete_path)
        camera.annotate_text = dt.datetime.now().strftime(timeFormat)
        camera.wait_recording(delta_record)
    camera.stop_recording()
