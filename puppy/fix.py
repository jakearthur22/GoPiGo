#this will contain the code for the exception
from puppy.func import kill

def keyboard():
  kill()
  print "Run ended! Keyboard Interrupt. \n Summary:"
  print "Variables: \n DESIRED_DIST: " + str(DESIRED_DIST[0]) + "," + str(DESIRED_DIST[-1]) + "\n MAX_DIST: " + str(MAX_DIST) + "\n Current Distance: " + str(dist())

def problem():
  kill()
  print "Run ended!"
  print str(type(e)) + ": " + str(e)
  print "\n Summary:"
  print "Variables: \n DESIRED_DIST: " + str(DESIRED_DIST[0]) + "," + str(DESIRED_DIST[-1]) + "\n MAX_DIST: " + str(MAX_DIST) + "\n Current Distance: " + str(dist())
