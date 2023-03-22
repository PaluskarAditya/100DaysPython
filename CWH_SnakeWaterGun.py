import random

res = {1: "Snake", 2: "Water", 3: "Gun"}

history = []
w = 0
l = 0
d = 0

i=1
while i <= 9:
    pc = random.randint(1, 3)
    for r in res:
        print(f"{r}: {res[r]}")

    resp = int(input("your choice: "))

    match resp:
        case 1:
            print(f"your choice: {res[1]}")
            if pc==1:
                print("pc choice: Snake")
                history.append("D")
            elif pc==2:
                print("pc choice: Water") 
                history.append("W")  
            elif pc==3:
                print("pc choice: Gun")  
                history.append("L")
            i+=1
        case 2:
            print(f"your choice: {res[2]}")
            if pc==1:
                print("pc choice: Snake")
                history.append("L")
            elif pc==2:
                print("pc choice: Water")  
                history.append("D") 
            elif pc==3:
                print("pc choice: Gun")
                history.append("W")
            i+=1   
        case 3:
            print(f"your choice: {res[3]}") 
            if pc==1:
                print("pc choice: Snake")
                history.append("W")
            elif pc==2:
                print("pc choice: Water")  
                history.append("L") 
            elif pc==3:
                print("pc choice: Gun")
                history.append("D")
            i+=1  
        case _:
            print("invalid choice")  
            history.append("D") 

    print()
    

print("checking results")

for h in history:
    if h=="W":
        w+=1
    elif h=="L":
        l+=1
    else:
        d+=1   

if w > l and w > d:
    print("You Won")
elif l > w and l > d:
    print("You Lost")   
else:
    print("Match Draw")                  

print("Game Over")               
