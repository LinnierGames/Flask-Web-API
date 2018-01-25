#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        title = word
        index = self._index(title)
        if index is not None:
            value = self[index][1]
            self[index] = (title, value + count)
        else:
            self.append((title, count))
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        index = self._index(word)

        return 0 if index is None else self[index][1]

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        title = str(word)

        return True if self._index(title) is not None else False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        found_index = None
        for i, element in enumerate(self):
            if element[0] == target:
                found_index = i
                break

        return found_index

    def sorted(self):
        """
        using bubble sort, sort by the count of repetitions of a word in a list
        :return: a new list of the sorted version of self
        """
        result = list(self)
        for iteration in range(len(result) - 1, 0, -1):
            for i in range(iteration):
                a = result[i]
                b = result[i + 1]
                if a[1] > b[1]:
                    temp = result[i]
                    result[i] = result[i + 1]
                    result[i + 1] = temp

        return result

    def writeToFile(self, filePath):
        """

        :param filePath:
        :return:
        """
        file = open(filePath, "w")
        for entry in self:
            file.write("'{}' repeats {} times\n".format(entry[0], entry[1]))
        file.close()



def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))

    print(histogram.sorted())
    print(histogram)
    histogram.writeToFile("textfile.txt")


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
