# -*- coding: utf-8 -*-
import random
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
        ========''','''
    
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        ========''','''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''','''
''']


WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]
def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        print()
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Prediste! La palabra correcta era: {}'.format(word))
                break
        else:
            for idxs in letter_indexes:
                hidden_word[idxs] = current_letter
            
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades! Ganastes. La palabra es: {}'.format(word))
            break

if __name__ == "__main__":
    print('A H O R C A D O S')
    run()