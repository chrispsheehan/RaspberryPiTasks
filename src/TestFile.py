import DateTime

import OS


def writeOut():
    dateTime = DateTime.dateStamp()

    OS.writeOutFile(dateTime)
    