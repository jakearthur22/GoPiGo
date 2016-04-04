#Main code for the GoPiGo
#Jacob Arthur
#SERVE ME, COMPUTER!!!

#Reminder: only use in an open space!
##################################################################################################
from gopigo import *
from time import sleep
import random
##################################################################################################
#set variables
DESIRED_DIST = range(61, 107)
MAX_DIST = 250
def dist():
    return us_dist(15)
s = -1
def set_servo(n):
    global s
    s = n
    servo(n)
def servo_val():
    return s
###################################################################################################
def idle():
    actions = ["rock", "rock", "look", "look", "rotate", "rotate", "nothing"]
    action = actions[random.randrange(0,7)]
    if(action == "rock"):
        for i in range(4):
            enc_tgt(1,1,1)
            fwd()
            sleep(.1)
            enc_tgt(1,1,1)
            bwd()
            sleep(.1)
    elif(action == "look"):
        servo(71)
        sleep(.5)
        servo(155)
        sleep(.5)
    elif(action == "rotate"):
        rot_choices = [right_rot, left_rot]
        rotation = rot_choices[random.randrange(0,2)]
        enc_tgt(1,1,3)
        rotation()
        sleep(.5)
    elif(action == "nothing"):
        sleep(1.5)
    servo(113)
    sleep(.2)
###################################################################################################
def checkLeftRight():
    set_servo(113)
    sleep(1)
    lost = False
    count = 0
    found = False
    for i in range(10):
        if(dist() in DESIRED_DIST): found = True
        else:
            pos = servo_val()
            set_servo(pos-12)
            sleep(.1)
            if(dist() in DESIRED_DIST): found = True
            else:
                set_servo(pos+12)
                sleep(.1)
                if(dist() in DESIRED_DIST): found = True
                else:
                    set_servo(pos-24)
                    sleep(.15)
                    if(dist() in DESIRED_DIST): found = True
                    else:
                        set_servo(pos+24)
                        sleep(.15)
                        if(dist() in DESIRED_DIST): found = True
                        else:
                            count += 1
                            if(count == 3):
                                lost = True
                                break
    pos = servo_val()
    if(lost):
        print "Target lost!"
        #spin()
    elif(pos<113):
        print "right"
        rot = int(round(float(113-pos) * .0694008))
        print rot
        servo(113)
        enc_tgt(1,1,rot)
        right_rot()
        sleep(.5)
        print "Target followed right."
    elif(pos>113):
        print "left"
        rot = int(round(float(pos-113) * .0694008))
        print rot
        servo(113)
        enc_tgt(1,1,rot)
        left_rot()
        sleep(.5)
        print "Target followed left."
####################################################################################################
def dance(): #cha cha?? and spin around 3 times
    print "I'm a dancin' machine!!!!!!!!"
    #test the versatility of the encoders.
    #try enc_tgt(1,0,x) + rot() instead of enc_tgt(1,1,x) + rot()
    #to make the bot thinks its rotating but its actually rotating around one wheel.
    #this will allow you to cha cha!
####################################################################################################
def runAway():
    #prepare in case against a wall
    servo(71)
    sleep(.6)
    right_dir = dist()
    servo(155)
    sleep(.6)
    left_dir = dist()
    if(left_dir > right_dir and left_dir > 30):
        print "Left!"
        left()
        sleep(1)
    elif(left_dir < right_dir and right_dir > 30):
        print "Right!"
        right()
        sleep(1)
    while True:
        servo(113)
        sleep(1)
        if(dist() > DESIRED_DIST[0]):
            print "Running!"
            fwd()
            sleep(1)
        else:
            print "Which way is clear??!"
            servo(71)
            sleep(1)
            right_dir = dist()
            servo(160)
            sleep(1)
            left_dir = dist()
            if(left_dir > right_dir and left_dir > 30):
                print "Left!"
                left()
                sleep(1)
            elif(left_dir < right_dir and right_dir > 30):
                print "Right!"
                right()
                sleep(1)
            else:
                print "No good!"
                rot_choices = [right_rot, left_rot]
                rotation = rot_choices[random.randrange(0,2)]
                rotation()
                sleep(1)
####################################################################################################
def scared():
    bwd()
    sleep(3)
    print "Now safe."
    while True:
        stop()
        servo(113)
        sleep(.5)
        #scared stuff
        while(dist() > DESIRED_DIST[-1]):
            print "Still scared..."
            idle()
            print "...."
            if(dist() > MAX_DIST):
                print "Can't see you!"
                checkLeftRight()
                print "Now safe."
        #dont follow, only back away
        if (dist() <= DESIRED_DIST[-1]): #the bot will stay away at a distance minimum the max in the normal range
            if(dist() <= 8):
                print "AAAAAHHHHHHHHHHHH!!!!!!!!"
                runAway()
            print "Too close!"
            adjust(bwd, True)
            print "Now safe."
####################################################################################################
def spin():
    found = False
    while(found == False):
        servo(71)
        sleep(.5)
        right_dir = dist()
        servo(155)
        sleep(.5)
        left_dir = dist()
        if(right_dir in DESIRED_DIST):
            print "Target found on the right."
            found = True
            servo(113)
            enc_tgt(1,1,3)
            right_rot()
            sleep(.5)
        elif(left_dir in DESIRED_DIST):
            print "Target found on the left."
            found = True
            servo(113)
            enc_tgt(1,1,3)
            left_rot()
            sleep(.5)
        else:
            print "Not here."
            rot_choices = [right_rot, left_rot]
            rotation = rot_choices[random.randrange(0,2)]
            rotation()
            sleep(.5)
####################################################################################################
def adjust(direction, frightened):
    if(frightened == False):
        while True:
            print "moving..."
            direction()
            sleep(1)
            if(dist() <= 6):
                scared()
            elif(dist() in DESIRED_DIST):
                break
        stop()
        print "moved."
    else:
        while True:
            print "backing away..."
            bwd()
            sleep(1)
            if(dist() <= 6):
                runAway()
            elif(dist() >= DESIRED_DIST[-1]):
                break
        stop()
        print "Now safe."
####################################################################################################
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
