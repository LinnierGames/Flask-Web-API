import random
random.seed(999)


# Picks from words file and randomly picks the given amount
class RandomWords(object):
    def __init__(self, num_words):
        super(RandomWords, self).__init__()

        with open("/usr/share/dict/words", "r") as f:
            str_words = f.read()

        arr_words = str_words.split('\n')
        int_word_array_size = len(arr_words)

        # arr_collection_of_selected_words = []
        str_collection_of_selected_words = ""

        for i in range(0, num_words):
            int_random_index = int(random.uniform(0, int_word_array_size -1))
            # arr_collection_of_selected_words.append(arr_words[int_random_index])
            str_collection_of_selected_words += arr_words[int_random_index] + ' '

        self.sentence = str_collection_of_selected_words

    def __str__(self):
        return self.sentence

