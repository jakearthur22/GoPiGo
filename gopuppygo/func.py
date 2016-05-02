#this will contain all of the code that uses the gopigo mechanical functions
from gopigo import *
from time import sleep
import random
###################################################################################################
DESIRED_DIST = range(61, 121)
MAX_DIST = 300
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
    sleep(.5)
    lost = False
    count = 0
    found = False
    for i in range(10):
        if(dist() < DESIRED_DIST[-1]): found = True
        else:
            print dist()
            print "Checking left and right.."
            pos = servo_val()
            set_servo(pos-12)
            sleep(.1)
            if(dist() < DESIRED_DIST[-1]): found = True
            else:
                set_servo(pos+12)
                sleep(.1)
                if(dist() < DESIRED_DIST[-1]): found = True
                else:
                    set_servo(pos-24)
                    sleep(.15)
                    if(dist() < DESIRED_DIST[-1]): found = True
                    else:
                        set_servo(pos+24)
                        sleep(.15)
                        if(dist() < DESIRED_DIST[-1]): found = True
                        else:
                            count += 1
                            if(count == 3):
                                lost = True
                                break
    pos = servo_val()
    if(lost):
        print "Target lost!"
        spin()
    elif(pos<113):
        rot = int(round(float(113-pos) * .0694008))
        servo(113)
        enc_tgt(1,1,rot)
        right_rot()
        sleep(.5)
        print "Target followed right."
    elif(pos>113):
        rot = int(round(float(pos-113) * .0694008))
        servo(113)
        enc_tgt(1,1,rot)
        left_rot()
        sleep(.5)
        print "Target followed left."
####################################################################################################
def dance():
    print "I'm a dancin' machine!!!!!!!!"
    servo(133)
    enc_tgt(1,1,2)
    right_rot()
    sleep(.5)
    servo(93)
    enc_tgt(1,1,2)
    left_rot()
    sleep(.5)
    servo(133)
    enc_tgt(1,1,2)
    right_rot()
    sleep(1)
    servo(93)
    enc_tgt(1,1,2)
    left_rot()
    sleep(.5)
    servo(133)
    enc_tgt(1,1,2)
    right_rot()
    sleep(.5)
    servo(93)
    enc_tgt(1,1,2)
    left_rot()
    sleep(1)
    #reset servo
    servo(113)
    sleep(.5)
    #spin and step and jump
    enc_tgt(1,1,18)
    right_rot()
    sleep(2)
    enc_tgt(1,0,2)
    right()
    sleep(1)
    enc_tgt(0,1,2)
    left()
    sleep(1)
    enc_tgt(1,1,1)
    fwd()
    sleep(.5)
    enc_tgt(1,1,1)
    bwd()
    sleep(.5)
    enc_tgt(1,1,1)
    fwd()
    sleep(.5)
    #spin and step and jump other direction
    enc_tgt(1,1,18)
    left_rot()
    sleep(2)
    enc_tgt(0,1,2)
    left()
    sleep(1)
    enc_tgt(1,0,2)
    right()
    sleep(1)
    enc_tgt(1,1,1)
    fwd()
    sleep(.5)
    enc_tgt(1,1,1)
    bwd()
    sleep(.5)
    enc_tgt(1,1,1)
    fwd()
    sleep(.5)
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
            stop()
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
                stop()
            elif(left_dir < right_dir and right_dir > 30):
                print "Right!"
                right()
                sleep(1)
                stop()
            else:
                print "No good!"
                rot_choices = [right_rot, left_rot]
                rotation = rot_choices[random.randrange(0,2)]
                rotation()
                sleep(1)
####################################################################################################
def scared():
    print "You scared me!"
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
            print dist()
            rot_choices = [right_rot, left_rot]
            rotation = rot_choices[random.randrange(0,2)]
            rotation()
            sleep(.5)
####################################################################################################
def adjust(direction, frightened):
    moving = True
    if(frightened == False):
        while moving:
            print "moving..."
            direction()
            sleep(.5)
            if(dist() <= 6):
                scared()
            elif(dist() in DESIRED_DIST):
                moving = False
        stop()
        print "moved."
    else:
        while moving:
            print "backing away..."
            bwd()
            sleep(.5)
            if(dist() <= 6):
                runAway()
            elif(dist() >= DESIRED_DIST[-1]):
                moving = False
        stop()
        print "Now safe."
####################################################################################################
def kill():
    stop()
    disable_servo()
    disable_encoders()
####################################################################################################
def reset():
    kill()
    enable_servo()
    enable_encoders()
    servo(113)
####################################################################################################
def run():
    while True:
        if (dist() <= 6):
            adjust(bwd, False)
            print "Startup complete."
            sleep(2)
            while True: #main autonymous loop. GoPiGo will follow you around!
                print "Following."
                servo(113)
                sleep(.5)
                if (dist() <= 6):
                    print "You scared me!"
                    scared()
                elif(dist() < DESIRED_DIST[0]): #if less than desired distance, but not obscured
                    print "Target moved closer."
                    adjust(bwd, False)
                    print "Backed up."
                elif(dist() > DESIRED_DIST[-1] and dist() < MAX_DIST): #if greater than desired distance, but target still in sight
                    print "Target moved away."
                    adjust(fwd, False)
                    print "Followed."
                elif(dist() in DESIRED_DIST):
                    print "Target in sight."
                    #check horizontal while in rest
                    checkLeftRight()
####################################################################################################
