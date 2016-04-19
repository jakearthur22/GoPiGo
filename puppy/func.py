#this will contain all of the code that uses the gopigo mechanical functions
from gopigo import *
from time import sleep
import random
###################################################################################################
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
    sleep(4)
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
    sleep(4)
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
def kill():
