import random

# Hangman stages
hangman_stages = [
    "",
    " O ",
    " O \n | ",
    " O \n\|/",
    " O \n\|/ \n | ",
    " O \n\|/ \n | \n/ \\"
]

# Functions
def main():
    print("Welcome to Hangman!")
    selected_film = get_random_film()
    print(f"Selected Film for debugging: {selected_film}")  # You can comment this out later.
    
    masked_film = mask_film(selected_film)
    guessed_letters = set()
    incorrect_guesses = 0
    
    while "#" in masked_film and incorrect_guesses < 5:
        print(f"The film name to guess is: {masked_film}")
        
        # Display hangman stage
        print(hangman_stages[incorrect_guesses])
        
        guess = input("Enter your guess (a letter or the entire name): ").lower()
        
        if len(guess) > 1:
            if guess == selected_film:
                print("Congratulations! You've guessed the entire film name!")
                return
            else:
                print("Incorrect full name guess.")
                incorrect_guesses += 1
                continue
        
        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in selected_film:
            print("Correct guess!")
            masked_film = update_masked_film(selected_film, guessed_letters)
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
    
    if incorrect_guesses == 5:
        print("Game Over!")
        print("The final hangman is:")
        print(hangman_stages[-1])
        print(f"The film was: {selected_film}")
    else:
        print(f"Congratulations! You've guessed the film: {selected_film}")


def get_random_film():
    films = ["endgame", "the lost boys", "donnie darko", "almost famous"]
    selected_film = random.choice(films)
    return selected_film.lower()

def mask_film(film_name):
    masked = ""
    for char in film_name:
        if char == " ":
            masked += " "
        else:
            masked += "#"
    return masked

def update_masked_film(film_name, guessed_letters):
    updated_masked = ""
    for char in film_name:
        if char in guessed_letters or char == " ":
            updated_masked += char
        else:
            updated_masked += "#"
    return updated_masked

# Run the main function to start the game
main()
