import gpio as GPIO
import runninglight
import time


#Pin for the light
MPIN = 3

#set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(MPIN, GPIO.OUT)

#create
rlm = runninglight.runninglightmanager(MPIN)

#run
rlm.set_mode(runninglight.light_mode.solid)
rlm.start()
print("Started!")
time.sleep(60)