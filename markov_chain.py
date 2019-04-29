from histogram import count_words
from dictogram import Dictogram

def get_words(filename):
    """Open the file
    and return a list of all words in it."""
    all_words_list = []
    with open(filename) as file:
        # go through one line at a time
        for line in file:
            #no arguement gets rid of all white spaces
            words_list = line.split()
            for word in words_list:
                all_words_list.append(word)
    return all_words_list

def markov_chain(words_list):
        """Count occurences in the given list of words and
        return that data structure"""
        # create new dictionary
        markov = {}
        # iterate over the corpus
        for i in range(len(words_list)-1):
        # create two variables for current word and current word + 1 (next)
            current_word = words_list[i]
            next_word = words_list[i+1]
            # check if word is key in dictionary
            if current_word in markov:
            # if key is in big dictionary, update Dictogram
                markov[current_word].add_count(next_word)
            # if word is not a key in dictionary, create key with value as dictogram
            else:
            # Dictogram key will be next with a value of 1
                markov[current_word] = Dictogram([next_word])
            # return dictionary
        return markov

if __name__ == '__main__':
    # word_list = get_words('Life.txt')
    word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
    histograms = markov_chain(word_list)
    print(histograms)
