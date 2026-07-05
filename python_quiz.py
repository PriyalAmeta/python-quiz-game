#quiz game and showing the results

print("----- Welcome User! -----")

ask = input("do you want to play the quiz game?? ")

if (ask.lower() != "yes"): #lowercasing the input cuz the user can enter yes or YES or Yes
    print("Terminating the quiz...")
    quit()
else:
    print("Starting the game...")

    result = 0 #initially its 0

    q1 = input("1. What is the capital of India? ")
    if(q1 != "New Delhi"):
        print("incorrect answer entered")
    else:
        print("That's correct!!")
        result = result + 1

    q2 = int(input("2. How many days are there in a leap year? "))
    if(q2 != 366):
        print("incorrect answer entered")
    else:
        print("That's correct!!")
        result = result + 1

    q3 = int(input("3. How many bones does an adult human have? "))
    if(q3 != 206):
        print("incorrect answer entered")
    else:
        print("That's correct!!")
        result = result + 1

    q4 = int(input("4. What is the square of 12? "))
    if(q4 != 144):
        print("incorrect answer entered")
    else:
        print("That's correct!!")
        result = result + 1
    
    q5 = int(input("5. How many sides does a hexagon have? "))
    if(q5 != 6):
        print("incorrect answer entered")
    else:
        print("That's correct!!")
        result = result + 1

print("----- End of the quiz -----")
print(f"you have scored {result} out of 5 !")
print(f" That's {result *100 /5}%") #showing percetage of correct answers
if(result >= 3):
    print("Well Done!!")
else:
    print("You can do better...")
    