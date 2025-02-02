from adafruit_servokit import ServoKit
import time

#class ServoTest():

#   see:    https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library
#          https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/library-reference


kit = ServoKit(channels=16)
servoNum = 15
sleepSeconds = 1

while True:

	kit.servo[servoNum].angle = 0
	time.sleep(sleepSeconds)
	kit.servo[servoNum].angle = 90
	time.sleep(sleepSeconds)
	kit.servo[servoNum].angle = 180
	time.sleep(sleepSeconds)
	kit.servo[servoNum].angle = 90
	time.sleep(sleepSeconds)


#    kit.servo[0].actuation_range = 160
#   set_pulse_width_range(min_pulse, max_pulse)
#   kit.servo[0].set_pulse_width_range(1000, 2000)

