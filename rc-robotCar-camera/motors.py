import curses
import RPi.GPIO as GPIO
from gpiozero import Motor

GPIO.setmode(GPIO.BCM)
motor1 = Motor(4, 14)
motor2 = Motor(17, 27)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                motor1.forward()
                motor2.forward()
            elif char == curses.KEY_DOWN:
                motor1.backward()
                motor2.backward()
            elif char == curses.KEY_LEFT:
                motor1.backward()
                motor2.forward()
            elif char == curses.KEY_RIGHT:
                motor1.forward()
                motor2.backward()
           
            
            elif char == ord('w'):
                motor1.forward()
                motor2.forward()
            elif char == ord("s"):
                motor1.backward()
                motor2.backward()
            elif char == ord('a'):
                motor1.backward()
                motor2.forward()
            elif char == ord('d'):
                motor1.forward()
                motor2.backward()
            

            elif char == 10:
                motor1.stop()
                motor2.stop()
        
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()