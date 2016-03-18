#And so it begins...
#Main code for the GoPiGo
#Jacob Arthur
#SERVE ME, COMPUTER!!!

#Reminder: only use in an open space!
#Reminder: may need a large flat board to be the target, because of the thinness of legs!
#Steps:
#First, check that the field of view is obscured by the target.
#This will set the target to the bot.
#Use a set distance to be the desired distance between bot and target.
#Reverse until the desired distance is met.
#Second, track the target moving forwards and backwards.                                ##RUN AWAY SCARED CODE BEFORE THIS
#Advance to desired distance if too far away, retreat to desired distance if too close.
#Third, track the target if it moves left or right.
#If the desired distance changes drastically due to the target moving out of the field of view,
#then oscilate the sensor left and right in increasing amounts
#(it may suffice to simply check half left and half right; or half, full, half, full; etc.) ##SPIN AROUND HERE
#check the distance.
#If it is close to the desired distance(or the desired distance has once again changed drastically),
#then rotate the entire bot in the direction of the target(by means of the angle of the sensor),
#simultaneously rotate the sensor back to forward facing position,
#then set the new target and advance or retreat to the desired distance.
#Repeat steps 2 and 3.

#Find ways to implement fun things, like spin around if target is not found, or random chance to run away from the target.

#SPIN AROUND
#if the target is not found through oscillation/rotation of the sensor,
#rotate the entire bot left or right(random) a set amount. ##implement and modify the code from the sample video
#then repeat the oscillation/rotation of the sensor and proceed within step 3.

#RUN AWAY SCARED
#If the target moves directly in front of the bot after initialization,
#then make the bot run away.
#Increase the distance, slowly move backwards, rock back and forth, turn head side to side, as if in panic
#after every action, check to see that the target is still at 12 o'clock.
#If the target is not at 12 o'clock, SPIN AROUND.
#If the target obscures the bot's vision again, completely run away. Implement code from sample video


##################################################################################################
from gopigo import *
from time import sleep
import random
##################################################################################################
#set variables
DESIRED_DIST = range(61, 107)
MAX_DIST = 200
def dist():
    return us_dist(15)

def rock():
    fwd()
    sleep(.2)
    stop()
    bwd()
    sleep(.2)
    stop()
###################################################################################################
###################################################################################################
def checkLeftRight():
    while True:
        servo(123) #slightly left
        sleep(.2)
        leftSide = dist()
        servo(103) #slightly right
        sleep(.2)
        rightSide = dist()
        if (rightSide > MAX_DIST and leftSide < MAX_DIST):
            return "left"
        elif (rightSide > MAX_DIST and leftSide > MAX_DIST):
            return "out of range"
        elif (rightSide > MAX_DIST and leftSide < MAX_DIST):
            return "right"
        else:
            print "I still see you! :)"
####################################################################################################
def dance(): #cha cha?? and spin around 3 times
    print "I'm a dancin' machine!!!!!!!!"
####################################################################################################
def runAway():
    #prepare in case against a wall
    servo(28)
    sleep(1)
    left_dir = dist()
    servo(112)
    sleep(1)
    right_dir = dist()
    if(left_dir > right_dir and left_dir > 30):
        print "Left!"
        left()
        sleep(1)
    elif(left_dir < right_dir and right_dir > 30):
        print "Right!"
        right()
        sleep(1)
    while noProblem:
        servo(70)
        sleep(1)
        if(dist() > DESIRED_DIST[0]):
            print "Running!"
            fwd()
            sleep(1)
        else:
            print "Which way is clear??!"
            servo(28)
            sleep(1)
            left_dir = dist()
            servo(112)
            sleep(1)
            right_dir = dist()
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
        servo(70)
        if(dist == 6):
            print "AAAAAHHHHHHHHHHHH!!!!!!!!"
            runAway()
        else:
            #scared stuff
            while(dist() > DESIRED_DIST[-1] or checkLeftRight != "fine"): #play around with this, you might still be able to make everything happen at once
                print "Still scared..."
                rock()
                rock()
                rock()
                servo(30) #look to one side
                sleep(1)
                servo(120) #look to the other side
                sleep(1)
                servo(70)
                sleep(1)
                print "...."
            #dont follow, only back away
            if (dist() <= DESIRED_DIST[-1]): #the bot will stay away at a distance minimum the max in the normal range
                print "Too close!"
                adjust(bwd, True)
                print "Now safe."
            else:
                #if the target moves left or right, turn to face it
                enable_encoders()
                check = checkLeftRight()
                if(check == "left"):
                    print "I saw you move left!"
                    enc_tgt(1,1,x)
                    left_rot()
                    sleep(1)
                    print "Now safe."
                elif(check == "right"):
                    print "I saw you move right!"
                    enc_tgt(1,1,x)
                    right_rot()
                    sleep(1)
                    print "Now safe."
                elif(check == "fine"):
                    print "Still scared..."
                else:
                    print "Unexpected value in checkLeftRight()"
                disable_encoders()
####################################################################################################
def spin():
    found = False
    while(found == False):
        servo(28)
        sleep(1)
        left_dir = dist()
        servo(112)
        sleep(1)
        right_dir = dist()
        if(left_dir in DESIRED_DIST):
            print "Target found."
            found = True
            enc_tgt(1,1,x) #rotate encoders x times to match the angle of the servo
            left_rot()
            sleep(1)
            servo(70)
            sleep(1)
        elif(right_dir in DESIRED_DIST):
            print "Target found."
            found = True
            enc_tgt(1,1,x) #rotate encoders x times to match the angle of the servo
            right_rot()
            sleep(1)
            servo(70)
            sleep(1)
        else:
            print "Not here."
            rot_choices = [right_rot, left_rot]
            rotation = rot_choices[random.randrange(0,2)]
            rotation()
            sleep(1)
####################################################################################################
def adjust(direction, scared): #there may be a way to do this with the encoders. Think about it!
    if(scared == False):
        while True:
            print "moving..."
            direction()
            sleep(1)
            if(dist() in DESIRED_DIST):
                break
        stop()
        print "moved."
    else:
        while True:
            print "backing away..."
            bwd()
            sleep(1)
            if(dist() >= DESIRED_DIST[-1]):
                break
        stop()
        print "Now safe."
####################################################################################################
try:
    print "Booting..."
    stop()
    enable_servo()
    #adjust the sensor to face front
    servo(70)
    print "Servo setup complete."
    #have the robot do a dance
    dance()
    stop()
    print "Dance sequence complete."
    #then start working after the sensor is obscured
    while True:
        if (dist() == 0):
            print finalState
            adjust(bwd, False)
            print "Startup complete."
        print "Following."
        while True: #main autonymous loop. GoPiGo will follow you around!
            servo(70)
            sleep(1)
            if (dist() == 0):
                print "You scared me!"
                scared()
            #check vertical
            elif(dist() < DESIRED_DIST[0]): #if less than desired distance, but not obscured
                print "Target moved closer."
                adjust(bwd, False)
                print "Backed up."
            elif(dist() > DESIRED_DIST[-1] and getDistance() < MAX_DIST): #if greater than desired distance, but target still in sight
                print "Target moved away."
                adjust(fwd, False)
                log("Followed.")
            elif(dist() in DESIRED_DIST):
                print "Desired distance reached."
                #check horizontal while in rest
                check = checkLeftRight()
                if (check == "left"):
                    print "Target went left."
                    #rotate left and adjust sensor
                    enable_encoders()
                    enc_tgt(1,0,x)
                    left_rot()
                    sleep(1)
                    disable_encoders()
                    servo(113)
                    sleep(1)
                    print "Target followed left."
                elif(check == "right"):
                    print "Target moved right."
                    #rotate right and adjust sensor
                    enable_encoders()
                    enc_tgt(0,1,x)
                    right_rot()
                    sleep(1)
                    disable_encoders()
                    servo(113)
                    sleep(1)
                    print "Target followed right."
                elif(check == "out of range"):
                    print "Target lost!"
                    spin()
                else:
                    print "Unexpected value in checkLeftRight()"
except KeyboardInterrupt:
    stop()
    disable_servo()
    disable_encoders()
    print "Run ended! Keyboard Interrupt. Summary: \n"
    print "Variables: \n DESIRED_DIST: " + str(DESIRED_DIST[0]) + "," + str(DESIRED_DIST[-1]) + "\n MAX_DIST: " + str(MAX_DIST) + "\n Current Distance: " + str(dist())
except:
    stop()
    disable_servo()
    disable_encoders()
    print "Run ended!. Summary: \n"
    print "Variables: \n DESIRED_DIST: " + str(DESIRED_DIST[0]) + "," + str(DESIRED_DIST[-1]) + "\n MAX_DIST: " + str(MAX_DIST) + "\n Current Distance: " + str(dist())
