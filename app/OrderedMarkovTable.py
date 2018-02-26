import sys
import re
import collections
from stochastic import Stochastic
from hashtable import HashTable


class OrderedMarkovChain(object):
    end_punctuation = [".","?","!"]

    def __init__(self, words, order):
        self.corpus = re.findall(r"[\w']+|[.,!?;]", words)
        self.words = HashTable(32)
        self.markov_order = order

        # iterate corpus
        previous_element = None
        previous_element_list = None
        if len(self.corpus) < self.markov_order + 1 and self.markov_order > 0:
            print("invalid corpus")
        else:
            max_iteration = len(self.corpus) - self.markov_order + 1
            for index in range(0, max_iteration):
                adjacent_index = index + self.markov_order
                current_element_list = self.corpus[index:adjacent_index]
                current_element = ' '.join(current_element_list)

                # check: at beginning of sentence, create/append current_word to self.words[None]
                if index == 0 or previous_element_list[0] in OrderedMarkovChain.end_punctuation:
                    stochastic_for_beginning_of_sentence = None
                    try:
                        stochastic_for_beginning_of_sentence = self.words[None]
                    except KeyError:
                        # stochastic for None is not made, so make one
                        stochastic_for_beginning_of_sentence = Stochastic()
                        self.words[None] = stochastic_for_beginning_of_sentence

                    stochastic_for_beginning_of_sentence.add_count(current_element)

                # grab adjacent word, can be None to represent end of the sentence

                def get_adjacent_word():
                    try:
                        adjacent_word = self.corpus[adjacent_index]
                        temp_list = current_element_list[1:] # current_element without the first index
                        temp_element = ' '.join(temp_list)

                        return adjacent_word
                    except IndexError:
                        # end of list_words, thus end of sentence
                        return None

                adjacent_element = get_adjacent_word()
                # print(current_element, "->{}".format(adjacent_element))

                # if current_word is an ending puncuation, then adjacent_word is None
                if current_element_list[-1] in OrderedMarkovChain.end_punctuation:
                    adjacent_element = None
                    # continue

                stochastic_for_current_word = None
                if current_element in self.words:
                    stochastic_for_current_word = self.words[current_element]
                else:
                    stochastic_for_current_word = Stochastic()
                    self.words[current_element] = stochastic_for_current_word

                stochastic_for_current_word.add_count(adjacent_element)
                previous_element = current_element
                previous_element_list = current_element_list

    def generate_a_sentence(self):
        sentence = ""

        if len(self.words) == 0:
            return sentence

        current_word = None

        # start sentence with None frequency
        current_word = self.words[None].choose_random_word_from_frequency()
        sentence += current_word

        current_word_list = current_word.split()

        prev_queue = collections.deque(current_word_list[:-1], maxlen=self.markov_order - 1)
        current_word = current_word_list[-1]

        while True:  # do-while
            prev_word = ' '.join(list(prev_queue))
            key = prev_word + " " + current_word if len(prev_word) != 0 else current_word
            prev_queue.append(current_word)
            stochastic = self.words[key]
            current_word = stochastic.choose_random_word_from_frequency()

            # check: end of sentence
            if current_word is None or current_word in OrderedMarkovChain.end_punctuation:
                # check: by a puncuation? if so, add it to the sentence
                if current_word in OrderedMarkovChain.end_punctuation:
                    sentence += current_word
                break
            else:
                pass
            sentence += " " + current_word

        return sentence


if __name__ == '__main__':
    m = OrderedMarkovChain("one fish two fish red fish blue fish.", 4)
    print(m.words)
    print("Sentence: {}".format(m.generate_a_sentence()))
