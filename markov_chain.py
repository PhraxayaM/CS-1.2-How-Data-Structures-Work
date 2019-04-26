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
        mc = Dictogram()

        for index in range(0, len(words_list)-1):
            word_index = word_list[index]
            if word_index in mc:
                mc[word_index].add_count(word_index)
            # Check if we saw this word before
            # next_word_index = index_tracker + 1
            # next_word = words_list[next_word_index]

            # if word in words_counts:
            #     words_counts
            #     # increase its count by one
            #     words_counts[word] += 1
            else:
                #set its count to one
                # words_counts[word] = 1
                new_mc = Dictogram()
                new_mc.add_count(word_index)
                mc[word_index] = new_mc
        return mc



if __name__ == '__main__':
    word_list = get_words('Life.txt')
    histograms = markov_chain(word_list)
    # print(histograms)
