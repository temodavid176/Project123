def random_python():
    import random
    numbers = [random.randint(0, 10) for i in range(5)]
    words = ['apple', 'banana', 'orange', 'grape', 'peach']
    for number in numbers:
        print(words[number])
