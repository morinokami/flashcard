import csv
import random


class Flashcard:
    def __init__(self, path):
        self.words = {}
        with open(path) as f:
            words = csv.reader(f)
            for word in words:
                self.words[word[0]] = word[1]

    def question(self):
        q = random.choice(list(self.words.keys()))
        a = self.words[q]
        dummy_q = q
        while dummy_q == q:
            dummy_q = random.choice(list(self.words.keys()))
        dummy_a = self.words[dummy_q]
        choices = [a, dummy_a]
        random.shuffle(choices)

        print('question: ' + q)
        print('choices: ', end='')
        for idx, choice in enumerate(choices):
            print('({}) {}  '.format(idx, choice), end='')
        print()
        try:
            user_a = input('your answer: ')
        except KeyboardInterrupt:
            print('\nbye')
            exit()
        while not user_a.isdigit() or int(user_a) not in range(len(choices)):
            print('hey, input can be either 0 or 1')
            try:
                user_a = input('your answer: ')
            except KeyboardInterrupt:
                print('\nbye')
                exit()
        if choices[int(user_a)] == self.words[q]:
            print('correct\n')
        else:
            print('wrong\n')


if __name__ == '__main__':
    cards = Flashcard('./words.csv')
    while True:
        cards.question()
