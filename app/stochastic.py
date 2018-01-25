from listogram import Listogram
import random


class Stochastic(Listogram):

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        self.__frequency_list = None
        super(Stochastic, self).__init__(word_list)  # Initialize this as a new list

    def frequency_of_tokens(self):
        # TODO: compare cached dic for any changes of self's components
        list_frequency = []
        max_number_entries = self.tokens

        for token_key, token_value in self:
            frequency = float(token_value) / float(max_number_entries)
            list_frequency.append((token_key, frequency))

        # Caching list
        self.__frequency_list = list_frequency

        return list_frequency

    def choose_random_word_from_frequency(self):
        """
        USAGE:
            0.0 <= 0.802293691502 <= 0.125
            0.125 <= 0.802293691502 <= 0.25
            0.25 <= 0.802293691502 <= 0.375
            0.375 <= 0.802293691502 <= 0.5
            0.5 <= 0.802293691502 <= 1.0
            fish
        :return: a word
        """
        list_stats = self.frequency_of_tokens()

        def item(i):
            return i[1]

        list_sorted_stats = sorted(list_stats, key=item)
        random_float = random.random()
        previous_tuple = None
        matching_word = None
        counter = 0
        cumulative_sum = 0
        last_count_in_sorted_list = len(list_sorted_stats) -1
        # // print(list_sorted_stats)

        for tuple_word_n_frequency in list_sorted_stats:
            start_value = 0.0 if previous_tuple is None else cumulative_sum
            end_value = tuple_word_n_frequency[1] + cumulative_sum if counter != last_count_in_sorted_list else 1.0

            #// print("{} <= {} <= {}".format(start_value,random_float,end_value))

            # is random_float between the values of the start point and the end point
            if start_value <= random_float <= end_value:
                matching_word = tuple_word_n_frequency[0]
                break
            else:
                previous_tuple = tuple_word_n_frequency
                counter += 1
                cumulative_sum += tuple_word_n_frequency[1]

        # must find a word within the random_float value
        # assert matching_word is not None

        return matching_word


if __name__ == '__main__':
    str_sentence = "one fish two fish red fish four fish"
    arr_sentence = str_sentence.split()

    stat = Stochastic(arr_sentence)
    print(stat.choose_random_word_from_frequency())