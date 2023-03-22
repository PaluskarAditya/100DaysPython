i=1
amount = 0
print("Welcome to KBC")
name = input("please enter your name: ")
prizeAmt = 10000
questions = ["What is the name of highest peak in the world?",
             "What is the current population of India?",
             "Who was the first person to land on Moon?",
             "Who was the first man to exist on Earth?"]

a1 = ["Mount Everest", "Mount Taboo", "Himalaya", "Mount Lhotse"]
a2 = ["122 Crore", "136 Crore", "1 Billion", "1.78 Million"]
a3 = ["Sunita Williams", "Matt Mulhock", "Arvind Kejriwal", "Neil Armstrong"]
a4 = ["Ancient Man", "Neanderthal Man", "Medieval Man", "Old Age Man"]

print("\n")
print(f"Okay {name}, Let's start")
print("\n")

for q in questions:
    print(f"Q{i}. {q} for {prizeAmt}")
    if i==1:
        for num, ans in enumerate(a1, start=1):
            print(f"{num}: {ans}")
        res = int(input("enter your answer: "))
        if res==1:
            print("Woah, you guessed it right!")
            amount+=prizeAmt
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")
        else:
            print("Sorry, you guessed it wrong")
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")
    elif i==2:
        for num, ans in enumerate(a2, start=1):
            print(f"{num}: {ans}")
        res = int(input("enter your answer: "))
        if res == 2:
            print("Woah, you guessed it right!")
            amount+=prizeAmt
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")
        else:
            print("Sorry, you guessed it wrong")
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")
    elif i==3:
        for num, ans in enumerate(a3, start=1):
            print(f"{num}: {ans}")
        res = int(input("enter your answer: "))
        if res == 4:
            print("Woah, you guessed it right!")
            amount+=prizeAmt
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")
        else:
            print("Sorry, you guessed it wrong")
            print(f"Your current winning amount is: {amount}")
            print("\n")
    elif i==4:
        for num, ans in enumerate(a4, start=1):
            print(f"{num}: {ans}")
        res = int(input("enter your answer: "))
        if res == 2:
            print("Woah, you guessed it right!")
            amount+=prizeAmt
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")
        else:
            print("Sorry, you guessed it wrong")
            print(f"Your current winning amount is: Rs.{amount}")
            print("\n")

    i+=1

print(f"The Final Prize taken by {name} is Rs.{amount}")
print("Thank You for being a part of KBC")