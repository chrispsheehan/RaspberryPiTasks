import os

import DateTime


def writeOutFile(dt_string):
    curentDir = os.path.dirname(os.path.realpath(__file__))

    targetOutFile = os.path.join(curentDir, "test.txt")

    file = open(targetOutFile, "w")
    file.write("Test job working :) - what a time to be alive!\n" + dt_string)
    file.close()


def writeOut():
    dateTime = DateTime.dateStamp()

    writeOutFile(dateTime)
