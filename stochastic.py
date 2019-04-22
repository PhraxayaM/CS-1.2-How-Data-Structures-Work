import random
import histogramlist



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


# finds a random word
def random_word(histogram):

    random_num = random.uniform(0, len(word_list))
    num = 0

    for word in histogram:
        count = histogram[word]
        num += count
        if num > random_num:
            return word

def count_words(words_list):
        """Count occurences in the given list of words and
        return that data structure"""
        words_counts = {}
        for word in words_list:
            # Check if we saw this word before
            if word in words_counts:
                # increase its count by one
                words_counts[word] += 1
            else:
                #set its count to one
                words_counts[word] = 1
        return words_counts


if __name__ == '__main__':

    """
    this is just an example Alan showed me on how spliting puts a string into a dictionary
    
    fish_list = 'one fish two fish red fish blue fish'.split()
    fish_histogram = count_words(fish_list)
     histogram = {'one':1, 'fish':1, 'blue':1, 'two':1, 'three':2, 'four':2}

     """
    word_list = get_words('Life.txt')
    histograms = count_words(word_list)
    words = []
    for _ in range(0, 8):
        words.append(random_word(histograms))
    print(words)
