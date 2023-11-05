def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark forest. What will you do?")
    print("1. Go deeper into the forest.")
    print("2. Turn back and leave.")

    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        forest_path()
    elif choice == '2':
        print("You leave the forest. Game over.")
    else:
        print("Invalid input. Please enter 1 or 2.")
        start_game()

def forest_path():
    print("You continue deeper into the forest and reach a clearing with three paths.")
    print("1. Take the left path.")
    print("2. Take the middle path.")
    print("3. Take the right path.")

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        print("You encounter a friendly squirrel. You've made a new friend!")
    elif choice == '2':
        print("You stumble upon a treasure chest. You're rich!")
    elif choice == '3':
        bear_encounter()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
        forest_path()

def bear_encounter():
    print("You encounter a fierce bear! What will you do?")
    print("1. Try to run away.")
    print("2. Play dead.")
    print("3. Stand your ground and make yourself look big.")

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        print("The bear chases you and you escape. You're safe!")
    elif choice == '2':
        print("The bear sniffs you but leaves. You survive!")
    elif choice == '3':
        print("The bear charges at you. Game over!")
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
        bear_encounter()

start_game()
