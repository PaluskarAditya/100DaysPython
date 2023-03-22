import random
import string

msg = input("enter your message: ")
type = input("1-Coding\n2-Decoding\n")

if type=='1':
    words = msg.split(" ")
    if len(words)>=3:
        rand1 = ''.join(random.choice(string.ascii_lowercase) for x in range(3))
        rand2 = ''.join(random.choice(string.ascii_lowercase) for x in range(3))
        char = msg[0]
        newStr = rand1 + msg[1:] + char + rand2
        print(f"message: {newStr[::-1]}")
    else:
        print(msg[::-1])    
elif type=='2':
    word = msg.split(" ")        
    if len(word)>=3:
        dec1 = msg[3:-3]
        dec2 = dec1[::-1]
        char = dec2[-1]
        final = char + dec2[:-1]
        print(f"message: {final}")
    else :
        print(msg[::-1])    
