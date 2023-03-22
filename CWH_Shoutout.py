import pyttsx3

names = ["aditya", "tanmay", "hemant", "harshali"]

eng = pyttsx3.init()

for name in names:
    eng.say(f"Shoutout to {name}")
    eng.runAndWait()

eng.say("Thank You Everybody")
eng.runAndWait()