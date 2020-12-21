import sys

import TestFile
import Setup

if len(sys.argv) == 2:

    firstArg = sys.argv[1]

    if firstArg == '-init':

        Setup.installPip()

        Setup.pipInstall(['crontab', 'requests'])

        Setup.installNode()        

    elif firstArg == '-test':

        TestFile.writeOut()    
        
    else:
        raise Exception("This logic path is not a thing. I'm a teapot.")

else:
    if len(sys.argv) <= 1:

        raise Exception("You need an arg, yer teapot!")

    else:

        raise Exception("Too many args, yer teapot!")    
