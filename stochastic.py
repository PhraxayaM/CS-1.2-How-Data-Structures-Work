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

    random_num = random.uniform(0, len(histogram))
    num = 0
    random_list = []

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

def sampling_frequency(histogram):
    word_check = {}
    for _ in range(13):
        word = random_word(histogram)
        if word in word_check:
            word_check[word] += 1
        else:
            word_check[word] = 1

    return word_check

def sample_markov(histogram):
    # Variable that sets the limit of the words frequency
    frequency_limit = 0
    # Unwrap the values inside the histogram by using .items(), we check for the key and values after unwrapping
    for key, value in histogram.items():
    # if our value "(key:value)" is higher than our frequency limit
        if value > frequency_limit:
            #set our frequency limit to be the same as our value
            frequency = value

    random_num = random.uniform(0, frequency_limit)

    while True:
        #choose a random index to check
        rand_index = random.randint(0, len(histogram) - 1)
        histogram_list = list(histogram)
        chosen_word = histogram_list[rand_index]

        if histogram[chosen_word] >= random_num:
            return chosen_word


if __name__ == '__main__':

    """
    this is just an example Alan showed me on how spliting puts a string into a dictionary

    fish_list = 'one fish two fish red fish blue fish'.split()
    fish_histogram = count_words(fish_list)
     histogram = {'one':1, 'fish':1, 'blue':1, 'two':1, 'three':2, 'four':2}

     """
    # words_list = get_words('Life.txt')
    # histograms = count_words(words_list)
    # test_freq = sampling_frequency(histograms)
    # test_markov = sample_markov(histograms)
    # words = []
    # for _ in range(0, 8):
    #     words.append(random_word(histograms))
    # print(words)
    # print(test_markov)
