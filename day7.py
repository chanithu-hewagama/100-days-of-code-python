import random
import hangman_art as art
import hangman_words as words
print(art.logo)
placeholding_character = "_"
def main():
    chosen_word = random.choice(words.word_list)
    print(chosen_word)
    placeholder = ""
    for i in range(0, len(chosen_word)):
        placeholder += placeholding_character
    print(placeholder)
    game_over = False
    correct_letters = []
    score = 6
    while not game_over:
        tmp_score = score
        guess = input("Guess a leter ").lower()
        print(guess)
        display = ""
        for each in chosen_word:
            
            if guess == each:
                display += guess
                correct_letters.append(guess)
            elif each in correct_letters:
                display += each
                
            else:
                display += placeholding_character
        if not guess in chosen_word:
            score -= 1
            print("Sorry, \"" + guess + "\" was not in the word.")
        elif guess in display:
            print("Whoops, you already guessed that letter.")
        print(art.stages[score])
        print(str(score) + "/6 Lives left!")    
        if not placeholding_character in display:
            print("You win.")
            game_over = True
        elif score == 0:
            print("You lose")
            game_over = True

        print(display)
if __name__ == "__main__":
    main()