from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("Hello (pi) World!")

print(dt_string)

import os

curentDir = os.path.dirname(os.path.realpath(__file__))

targetOutFile = os.path.join(curentDir, "test.txt")

file = open(targetOutFile, "w") 
file.write("This file was created to make sure the boot task is working today\n" + dt_string) 
file.close()