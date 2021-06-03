import random

class Words:
    """
    The Words class puts the words in the words.txt file into a list and returns a word from that list.
    """

    def __init__(self):
        self.words = []
        self.next_word = ""
        self.generate_list()

    def generate_list(self):
        words = open("game/words.txt", "r")
        for word in words:
            self.words.append(word)

        words.close()

    def get_next_word(self):
        self.next_word = self.words[random.randint(0,9999)]
        return self.next_word
