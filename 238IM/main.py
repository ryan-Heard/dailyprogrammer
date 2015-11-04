import random

def get_list(level):
    possible = []
    final_list = []
    word_level_dict = {1: (4, 5), 2: (6,7, 8), 3: (9,10,11), 4: (12, 13), 5: (14, 15)}
    num_of_words = {1: (5, 6), 2: (7, 8), 3: (9, 10, 11), 4: (12, 13), 5: (14, 15)}
    word_size = random.choice(word_level_dict[level])

    with  open("enable1.txt") as file:
        for line in file:
            if len(line.strip()) == word_size:
                possible.append(line.strip().upper())

    random.shuffle(possible)

    for i in range(0, random.choice(num_of_words[level])):
        final_list.append(possible[i])

    return final_list

def guess(guess, key):
    guess = guess.upper()
    correct = 0

    for user_letter,actual in zip(guess,key):
        if user_letter == actual:
            correct += 1

    print str(correct)+'/'+str(len(key))
    if correct == len(key):
        return True
    else:
        return False

def game():
    level_selection = eval(raw_input("Enter difficulty (1-5): "))
    the_list = get_list(level_selection)
    the_correct_word = the_list[random.randrange(0,len(the_list))]

    for word in the_list:
        print (word +'\n')

    for i in range(0,4):
        attempt = raw_input("Guess Word: ")
        result = guess(attempt,the_correct_word )
        if result:
            return True

    return the_correct_word

def main():
     gameResults = game()

     if(gameResults == True):
         print("You win!")
     else:
        print("The correct word was: "+gameResults)

main()
