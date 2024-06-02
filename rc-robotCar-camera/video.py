from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1920, 1080)
camera.framerate = 24

camera.start_preview()
camera.start_recording('/home/phil/Desktop/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()