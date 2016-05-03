#this is the main code through which all other code will run
import func
import fix

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
except Exception:
    print "Error importing. Code needs maintenance."
