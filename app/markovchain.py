import sys
sys.path.insert(0,"../4-exercies")
import random
from stochastic import Stochastic


class Markov(object):

    def __init__(self, list_words=None):

        self.corpus = list_words
        self.words = {} # [String: Stochastic]

        # iterate corpus
        for index, current_word in enumerate(self.corpus):
            adjacent_word = None  # None is equal to stop

            def get_adjacent_word():
                try:
                    # TODO: end of sentence
                    return self.corpus[index + 1]
                except IndexError:
                    return None

            # TODO: identify the beginning of a sentence

            adjacent_word = get_adjacent_word()

            stochastic_for_current_word = None
            if current_word in self.words:
                stochastic_for_current_word = self.words[current_word]
            else:
                stochastic_for_current_word = Stochastic()
                self.words[current_word] = stochastic_for_current_word

            stochastic_for_current_word.add_count(adjacent_word)

    def generate_a_sentence(self):
        sentence = ""

        # pick a random starting word
        sentence = current_markov = self.words.keys()[random.randint(0,len(self.words) - 1)]

        while current_markov is not None:
            stochastic = self.words[current_markov]
            current_markov = stochastic.choose_random_word_from_frequency()
            if current_markov is not None:
                sentence += " " + current_markov

        return sentence


if __name__ == '__main__':
    m = Markov("one fish two fish red fish blue fish".split())
    print(m.generate_a_sentence())
