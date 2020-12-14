from datetime import datetime

def dateStamp() :
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    print("Hello (pi) World!")

    print(dt_string)

    return dt_string