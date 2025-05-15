while True: #Asks for the input from the user 
    answer = input("State three extinct animals: ")

    if answer == "Dodo":
       print("Yes, the Dodo has been extinct since around 1690, according to sources.")
       break 
    elif answer == "Woolly Mammoths":
       print("Correct, the Woolly Mammoths have been extinct in Siberia since 10,000 years ago.")
       break 
    elif answer ==  "Golden Toad":
       print("Right, the Golden Toad's last sighting was in the 1980s.")
       break 
    else:
       print("Try again") 
    
print("Nice job!")