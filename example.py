import RPi.GPIO as GPIO
import runninglightcontrol
import time


#Pin for the light
MPIN = 3

#set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(MPIN, GPIO.OUT)

#create
rlm = runninglightcontrol.runninglightmanager(MPIN)

#run
rlm.set_mode(runninglightcontrol.light_mode.doubleblink_1sec)
rlm.start()
print("Started!")
time.sleep(5)
rlm.set_mode(runninglightcontrol.light_mode.solid)
time.sleep(60)
