import time

def Greet():
    currTime = int(time.strftime("%H"))

    if currTime >= 5 and currTime < 12:
        print("Good Morning Sir")
    elif currTime >= 13 and currTime < 16:
        print("Good Afternoon Sir")
    elif currTime >= 16 and currTime <= 19:
        print("Good Evening Sir")
    else:
        print("Good Night Sir")

Greet()