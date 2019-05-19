from histogram import count_words
from histogram import get_words
from dictogram import Dictogram
import random
import stochastic

def markov_chain(words_list):
        """Count occurences in the given list of words and
        return that data structure"""
        # create new dictionary
        markov = {}
        # iterate over the corpus
        for index in range(len(words_list)-2):
        # create two variables for current word and current word + 1 (next)
            # print(words_list)
            current_word = (words_list[index], words_list[index+1])
            print(current_word)
            next_word = words_list[index+2]
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

def next_word(chain, starting_words):
    # pick a random int
    if starting_words not in chain:
        return

    word_dict = chain[starting_words]
    max_freq = max(word_dict.values())
    rand_frequency = random.uniform(0, max_freq)
    list_from_words = list(word_dict)
    while True:
        rand_index = random.randint(0, len(word_dict) - 1)
        selected_word = list_from_words[rand_index]
        if word_dict[selected_word] >= rand_frequency:
            return selected_word

def make_sentence(chain, starting_words, sentence_len):
    previous_words = starting_words
    selected_list = [starting_words[0], starting_words[1]]
    for _ in range(sentence_len - 2):
        selected_word = next_word(chain, previous_words)
        if selected_word is not None:
            selected_list.append(selected_word)
            previous_words = (previous_words[1], selected_word)
    sentence = ' '.join(selected_list)
    return sentence

if __name__ == '__main__':
    word_list = get_words('life.txt')
    chain = markov_chain(word_list)
    list_from_chain = list(chain)
    random_words = random.choice(list_from_chain)
    # # print(random_words)
    sentence = make_sentence(chain, random_words, 5)
    print(sentence)
