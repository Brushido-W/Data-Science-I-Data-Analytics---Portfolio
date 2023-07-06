import random

word_categories = {
    "Car brands": ["ford", "honda", "toyota", "bmw", "audi"],
    "Fruits": ["apple", "banana", "cherry", "orange", "mango"],
    "Vegetables": ["carrot", "potato", "broccoli", "tomato", "cabbage"],
    "Clothing brands": ["nike", "adidas", "gucci", "zara", "levis"],
    "Colours": ["red", "blue", "green", "yellow", "purple"],
    "Countries": ["usa", "canada", "germany", "japan", "brazil"],
    "Animals": ["cat", "dog", "elephant", "lion", "tiger"],
    "Sports": ["soccer", "basketball", "tennis", "swimming", "volleyball"],
    "Professions": ["doctor", "teacher", "engineer", "artist", "chef"],
    "Movies": ["avatar", "inception", "titanic", "jaws", "star wars"],
    "Planets": ["mercury", "venus", "mars", "jupiter", "neptune"],
    "Languages": ["english", "spanish", "french", "german", "japanese"],
    "Shapes": ["circle", "triangle", "square", "rectangle", "hexagon"],
    "Musical Instruments": ["guitar", "piano", "drums", "violin", "trumpet"],
    "Books": ["harry potter", "lord of the rings", "to kill a mockingbird", "1984", "pride and prejudice"]
}

def choose_word(category):
    """
    Selects a random word from the specified category.

    Args:
        category (str): The chosen category of words.

    Returns:
        str: The randomly chosen word from the category.
    """
    word_list = word_categories.get(category)
    if word_list:
        return random.choice(word_list)
    else:
        return None

def display_categories():
    """
    Displays the available categories.
    """
    print("Available categories:")
    for category in word_categories.keys():
        print(category)

def get_category():
    """
    Prompts the player to choose a category.

    Returns:
        str: The chosen category.
    """
    while True:
        category = input("Choose a category: ")
        if category in word_categories.keys():
            return category
        else:
            print("Invalid category. Please choose a valid category.")

def initialize_game():
    """
    Initializes the game by selecting a category and word, and setting up the initial variables.

    Returns:
        Tuple[str, list, int]: The word, list of guesses, and number of tries.
    """
    category = get_category()
    word = choose_word(category)
    guesses = []
    tries = 6
    return word, guesses, tries

def display_word(word, guesses):
    """
    Displays the current state of the word with blanks for unguessed letters.

    Args:
        word (str): The word to guess.
        guesses (list): List of guessed letters.
    """
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    print(display)

def get_guess():
    """
    Prompts the player to enter a letter guess.

    Returns:
        str: The letter guessed by the player.
    """
    while True:
        guess = input("Guessa letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        else:
            return guess

def check_guess(guess, word, guesses):
    """
    Checks if the guessed letter is in the word.

    Args:
        guess (str): The letter guessed by the player.
        word (str): The word to guess.
        guesses (list): List of guessed letters.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    if guess in guesses:
        print("You already guessed that letter!")
    elif guess in word:
        guesses.append(guess)
        return True
    else:
        guesses.append(guess)
        return False

def check_win(word, guesses):
    """
    Checks if the player has won the game.

    Args:
        word (str): The word to guess.
        guesses (list): List of guessed letters.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for letter in word:
        if letter not in guesses:
            return False
    return True

def draw_hangman(tries):
    """
    Displays the hangman figure based on the remaining number of tries.

    Args:
        tries (int): The remaining number of tries.
    """
    stages = [
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \.
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    print(stages[tries])

def play_game():
    """
    Plays the Hangman game.
    """
    print("Welcome to Hangman!")
    display_categories()
    word, guesses, tries = initialize_game()
    while tries > 0:
        print(f"Tries left: {tries}")
        display_word(word, guesses)
        guess = get_guess()
        if check_guess(guess, word, guesses):
            print("Correct guess!")
        else:
            tries -= 1
            print("Wrong guess!")
            if tries > 0:
                draw_hangman(tries)  # Display the hangman figure after a wrong guess
        if check_win(word, guesses):
            print("Congratulations! You won!")
            return
    print("Game over! You ran out of tries.")
    print(f"The word was: {word}")

play_game()
