import random
import sys

# read the contents of the text document
f = open('https://api.diffbot.com/v3/analyze?token=861799482fc1e5a2f83d577f59fc6531&url=https://southpark.fandom.com/wiki/Cartman_Gets_an_Anal_Probe/Script', 'r')
content = f.readlines()
f.close()

# variable to take in argument from command land to search for how many words to find
word_count = int(sys.argv[1])

#empty array. Used to add(append) random words that are found
random_words_list = []

#this finds a random word. It takes in the word_count parameter and then searches the whole document after picking a random interger between 0 and the size of the content
def choose_random_words():
    for num in range(word_count):
        rand_index = random.randint(0, len(content) - 1)
        random_words_list.append(content[rand_index].rstrip())
    return


if __name__ == '__main__':
    choose_random_words()
    print(random_words_list)
    makesentence = ' '.join(random_words_list)
    print(makesentence)
