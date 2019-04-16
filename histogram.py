from pprint import pprint

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



words_list = get_words('LifeAndHabit.txt')
counts = count_words(words_list)
# print(get_words('LifeAndHabit.txt'))
# print(counts['works'])
# print(counts)


histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]

def histograma(lst):
    for word_list in lst:
        print("{}:{}".format([word_list[0]],[word_list[1]]))

def count_words(words_list):
    """Count occurences in the given list of words and
    return that data structure"""

    words_counts = {}

    for word_name in words_list:
        # Check if we saw this word before
        if word_name in words_counts:
            # increase its count by one
            words_counts[word_name] += 1
        else:
            #set its count to one
            words_counts[word_name] = 1

    return ["{}:{}".format([word_name[0]],[word_name[1]])]

# histogram = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
#
# def histogramaTuple(tpl):
#     for word_list in tpl:
#         print("{}:{}".format(word_list[0],word_list[1]))

# histograma(histogram)
# histogramaTuple(histogram)

words_list = get_words('LifeAndHabit.txt')
counts = count_words(histogram)
print(counts)
