#this is the main code through which all other code will run
import func
import fix

def ex():
    try:
        print "Booting..."
        func.reset()
        print "Servo setup complete."
        func.dance()
        print "Dance sequence complete."
        func.run()
    except KeyboardInterrupt:
        fix.keyboard()
    except Exception as e:
        fix.problem()
    except ImportError:
        print "Files not installed correctly."
        print "Please make sure to install all files and keep"
        print "them in the 'gopuppygo' folder."

ex()
