#####################################
##        START ROLL               ##
#####################################
## This will return which player   ##
## will be the first move.  This   ##
## is denoted by a 1 for Player 1  ##
## and a 2 for Player 2            ##
#####################################

import random
x = random.randrange(1,11)

def StartRoll():
    if x >= 5:
        return 2
        print 2
    else:
        return 1
        print 1
    

