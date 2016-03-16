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
from time import sleep()
import random
##################################################################################################
#set variables
runName = ""
logStr = ""
DESIRED_DIST = range(61, 107)
MAX_DIST = 200
finalState = "none"
noProblem = True
def getDistance():
    return us_dist(15)

def rock():
    fwd()
    sleep(.2)
    stop()
    bwd()
    sleep(.2)
    stop()
    
def log(x):
    print x
    x += "\n"
    logStr += x
###################################################################################################
###################################################################################################
#main autonymous loop. GoPiGo will follow you around!
def followMe():
    finalState = "Following"
    log("Following.")
    while noProblem:
        stop()
        servo(70)
        sleep(1)
        if (getDistance() <= 3):
            log("You scared me!")
            scared()
        #check vertical
        elif(getDistance() > 3 and getDistance() < DESIRED_DIST[0]): #if less than desired distance, but not obscured
            log("Target moved closer.")
            adjust(bwd, False)
            log("Backed up.")
        elif(getDistance() > DESIRED_DIST[-1] and getDistance() < MAX_DIST): #if greater than desired distance, but target still in sight
            log("Target moved away.")
            adjust(fwd, False)
            log("Followed.")
        elif(getDistance() in DESIRED_DIST):
            log("Desired distance reached.")
            #check horizontal while in rest
            check = checkLeftRight()
            if (check == "left"):
                log("Target went left.")
                #rotate left and adjust sensor
                enable_encoders()
                enc_tgt(1,0,x)
                left()
                sleep(1)
                disable_encoders()
                servo(70)
                sleep(1)
                log("Target followed left.")
            elif(check == "right"):
                log("Target moved right.")
                #rotate right and adjust sensor
                enable_encoders()
                enc_tgt(0,1,x)
                right()
                sleep(1)
                disable_encoders()
                servo(70)
                sleep(1)
                log("Target followed right.")
            elif(check == "out of range"):
                log("Target lost!")
                spin()
            elif(check == "fine"):
                #back to top of while loop.
            else:
                noProblem = False
        else:
            noProblem = False
    if(!noProblem):
        stop()
        disable_servo()
        print "ERROR ERROR ERROR ERROR: Something went wrong. Loops not reached."
        print read_status()
        print "Run ended."

####################################################################################################
def checkLeftRight():
    servo(50) #slightly left
    sleep(.4)
    leftSide = getDistance()
    servo(90) #slightly right
    sleep(.4)
    rightSide = getDistance()
    if (leftSide > MAX_DIST and rightSide < MAX_DIST):
        return "right"
    elif (rightSide > MAX_DIST and leftSide < MAX_DIST):
        return "left"
    elif (rightSide > MAX_DIST and leftSide > MAX_DIST):
        return "out of range"
    elif (rightSide < MAX_DIST and leftSide < MAX_DIST):
        return "fine"
    else: #somebody done goofed
        return "done goofed"
####################################################################################################
def dance(): #cha cha?? and spin around 3 times
    finalState = "Dancing"
####################################################################################################
def runAway():
    finalState = "Running away!"
    #prepare in case against a wall
    servo(28)
    sleep(1)
    left_dir = getDistance()
    servo(112)
    sleep(1)
    right_dir = getDistance()
    if(left_dir > right_dir and left_dir > 30):
        log("Left!")
        left()
        sleep(1)
    elif(left_dir < right_dir and right_dir > 30):
        log("Right!")
        right()
        sleep(1)
    while noProblem:
        servo(70)
        sleep(1)
        if(getDistance() > DESIRED_DIST[0])
        log("Running!")
        fwd()
        sleep(1)
        else:
            log("Which way is clear??!")
            servo(28)
            sleep(1)
            left_dir = getDistance()
            servo(112)
            sleep(1)
            right_dir = getDistance()
            if(left_dir > right_dir and left_dir > 30):
                log("Left!")
                left()
                sleep(1)
            elif(left_dir < right_dir and right_dir > 30):
                log("Right!")
                right()
                sleep(1)
            else:
                log("No good!")
                rot_choices = [right_rot, left_rot]
                rotation = rot_choices[random.randrange(0,2)]
                rotation()
                sleep(1)
####################################################################################################
def scared():
    finalState = "Scared"
    bwd()
    sleep(3)
    log("Now safe.")
    while noProblem:
        stop()
        servo(70)
        if(getDistance() == 6):
            log("AAAAAHHHHHHHHHHHH!!!!!!!!")
            runAway()
        else:
            #scared stuff
            enable_encoders()
            while(getDistance() > DESIRED_DIST[-1] or checkLeftRight != "fine"):
                log("Still scared...")
                rock()
                rock()
                rock()
                servo(30) #look to one side
                sleep(1)
                servo(120) #look to the other side
                sleep(1)
                servo(70)
                sleep(1)
                log("....")
            disable_encoders()
            #dont follow, only back away
            if (getDistance() <= DESIRED_DIST[-1]): #the bot will stay away at a distance minimum the max in the normal range
                log("Too close!")
                adjust(bwd, True)
                log("Now safe.")
            else:
                #if the target moves left or right, turn to face it
                check = checkLeftRight()
                if(check == "left"):
                    log("I saw you move left!")
                    enc_tgt(1,1,x)
                    left_rot()
                    sleep(1)
                    log("Now safe.")
                elif(check == "right"):
                    log("I saw you move right!")
                    enc_tgt(1,1,x)
                    right_rot()
                    sleep(1)
                    log("Now safe.")
                else:
                    noProblem = False
    if(!noProblem):
        stop()
        disable_servo()
        print "ERROR ERROR ERROR ERROR: Something went wrong. Loops not reached."
        print read_status()
        print "Run ended."
####################################################################################################
def spin():
    found = False
    while !found:
        servo(28)
        sleep(1)
        left_dir = getDistance()
        servo(112)
        sleep(1)
        right_dir = getDistance()
        if(left_dir in DESIRED_DIST):
            log("Target found.")
            found = True
            enc_tgt(1,1,x) #rotate encoders x times to match the angle of the servo
            left_rot()
            sleep(1)
            servo(70)
            sleep(1)
        elif(right_dir in DESIRED_DIST):
            log("Target found.")
            found = True
            enc_tgt(1,1,x) #rotate encoders x times to match the angle of the servo
            right_rot()
            sleep(1)
            servo(70)
            sleep(1)
        else:
            log("Not here.")
            rot_choices = [right_rot, left_rot]
            rotation = rot_choices[random.randrange(0,2)]
            rotation()
            sleep(1)
####################################################################################################
def adjust(direction, scared): #there may be a way to do this with the encoders. Think about it!
    done = False
    if !scared:
        while !done:
            log("moving...")
            direction()
            sleep(1)
            if(getDistance() in DESIRED_DIST):
                done = True
        log("moved.")
    else:
        while !done:
            log("backing away...")
            bwd()
            sleep()
            if(getDistance() >= DESIRED_DIST[-1]):
                done = True
        log("Now safe.")
####################################################################################################
def startup():
    log("Booting...")
    stop()
    enable_servo()
    #adjust the sensor to face front
    servo(70)
    log("Servo setup complete.")
    #have the robot do a dance
    dance()
    stop()
    log("Dance sequence complete.")
    #then start working after the sensor is obscured
    while noProblem:
        if (getDistance() == 0):
            adjust(bwd, False)
            log("Startup complete.")
            followMe()
####################################################################################################

try:
    runName = raw_input("Plase name this run: ")
    runName = "run_log_" + runName
    startup()
except KeyboardInterrupt:
    log("Run ended!. Summary: \n" + read_status() + "\n")
    log("Variables: \n DESIRED_DIST: " + DESIRED_DIST + "\n MAX_DIST: " + MAX_DIST + "\n Current Distance: " + getDistance() + "\n Final State Reached: " + finalState)
    #create a file with a log of all the activity.
    outfile = file(runName, "w")
    outfile.write(logStr)
except:
    log("Error reached. Summary: \n" + read_status() + "\n")
    log("Variables: \n DESIRED_DIST: " + DESIRED_DIST + "\n MAX_DIST: " + MAX_DIST + "\n Current Distance: " + getDistance() + "\n Final State Reached: " + finalState)
    #create a file with a log of all the activity.
    outfile = file(runName, "w")
    outfile.write(logStr)
