import sys

import TestFile

if len(sys.argv) == 2:
    if sys.argv[1] == '-init':
        TestFile.writeOut()
    else:
        raise Exception("This logic path is not a thing. I'm a teapot.")

else:
    if len(sys.argv) <= 1:
        raise Exception("You need an arg, yer teapot!")
    else:
        raise Exception("Too many args, yer teapot!")    