import os
import picamera
import datetime as dt
from numpy import inf

def get_fs_freespace(pathname):
    "Gets the free space of the filesystem containing pathname"
    stat = os.statvfs(pathname)
    return stat.f_bfree*stat.f_bsize

def get_oldest_file(pathname):
    "Gets the oldest file in the path"
    filename = min(os.listdir(pathname), key=lambda p: os.path.getctime(os.path.join(pathname,p)))
    filename = os.path.join(pathname, filename)
    return filename

width = 1600
height = 900
frameRate = 24
filePath = '/media/pi/PNY-128G/data/'
fileNameFormat = '%Y-%m-%d--%H.h264'
timeFormat = '%Y-%m-%d %H:%M:%S'
duration = inf
delta_record = .5
previewVideo = False
# Threshold before deleting the oldest file
rotateThreshold = 10000000000

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
        if get_fs_freespace(filePath) < rotateThreshold:
            os.remove(get_oldest_file(filePath))
        if past_hour != dt.datetime.now().hour:
            past_hour = dt.datetime.now().hour
            current_time = dt.datetime.now()
            fileName = current_time.strftime(fileNameFormat)
            complete_path = filePath + fileName
            camera.split_recording(complete_path)
        camera.annotate_text = dt.datetime.now().strftime(timeFormat)
        camera.wait_recording(delta_record)
    camera.stop_recording()

