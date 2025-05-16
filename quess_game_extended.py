while True:
    guess = input("Please enter your guess (or type 'quit' to exit): ")
    
    if guess.lower() == 'quit':
        print("Thank you for playing")
        break

    # You can keep your existing guess validation and game logic below
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # ... rest of your guessing logic ...
