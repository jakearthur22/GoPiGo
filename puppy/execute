#this is the main code through which all over code will run
from func import dist
from func import reset
from func import 
import except

try:
    print "Booting..."
    stop()
    enable_servo()
    enable_encoders()
    #adjust the sensor to face front
    servo(113)
    print "Servo setup complete."
    #have the robot do a dance
    dance()
    stop()
    print "Dance sequence complete."
    #then start working after the sensor is obscured
    while True:
        if (dist() <= 6):
            adjust(bwd, False)
            print "Startup complete."
            while True: #main autonymous loop. GoPiGo will follow you around!
                print "Following."
                servo(113)
                sleep(.5)
                if (dist() <= 6):
                    print "You scared me!"
                    scared()
                #check vertical
                elif(dist() < DESIRED_DIST[0]): #if less than desired distance, but not obscured
                    print "Target moved closer."
                    adjust(bwd, False)
                    print "Backed up."
                elif(dist() > DESIRED_DIST[-1] and dist() < MAX_DIST): #if greater than desired distance, but target still in sight
                    print "Target moved away."
                    adjust(fwd, False)
                    print "Followed."
                elif(dist() in DESIRED_DIST):
                    print "Desired distance reached."
                    #check horizontal while in rest
                    print "Checking left and right..."
                    checkLeftRight()
except KeyboardInterrupt:
    stop()
    disable_servo()
    disable_encoders()
    print "Run ended! Keyboard Interrupt. \n Summary:"
    print "Variables: \n DESIRED_DIST: " + str(DESIRED_DIST[0]) + "," + str(DESIRED_DIST[-1]) + "\n MAX_DIST: " + str(MAX_DIST) + "\n Current Distance: " + str(dist())
except Exception as e:
    stop()
    disable_servo()
    disable_encoders()
    print "Run ended!"
    print str(type(e)) + ": " + str(e)
    print "\n Summary:"
    print "Variables: \n DESIRED_DIST: " + str(DESIRED_DIST[0]) + "," + str(DESIRED_DIST[-1]) + "\n MAX_DIST: " + str(MAX_DIST) + "\n Current Distance: " + str(dist())
