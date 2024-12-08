def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead:")
    print("1. Take the left path.")
    print("2. Take the right path.")
    
    choice = input("Enter 1 or 2 to choose a path: ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice! Please restart the game and choose 1 or 2.")
        return

def left_path():
    print("\nYou take the left path and come across a wild wolf!")
    print("You can:")
    print("1. Try to fight the wolf.")
    print("2. Run away.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        print("\nYou try to fight the wolf but it's too strong. You lose!")
    elif choice == "2":
        print("\nYou run away and safely find your way out of the forest. You win!")
    else:
        print("Invalid choice! The wolf attacks you. Game over.")

def right_path():
    print("\nYou take the right path and find a treasure chest!")
    print("You can:")
    print("1. Open the chest.")
    print("2. Leave it alone and continue walking.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        print("\nYou open the chest and find a pile of gold! You win!")
    elif choice == "2":
        print("\nYou walk away and safely leave the forest, but you miss the treasure. Game over.")
    else:
        print("Invalid choice! You wander aimlessly and get lost. Game over.")

# Start the game
start_game()
