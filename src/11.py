import random

def get_random_word():
    with open('words.txt', 'r') as file:
        words = [word.strip() for word in file]
    return random.choice(words)