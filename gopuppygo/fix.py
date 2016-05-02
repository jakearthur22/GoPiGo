#this will contain the code for the exception
from func import kill
from func import dist
from func import DESIRED_DIST
from func import MAX_DIST
from gopigo import us_dist

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
  
