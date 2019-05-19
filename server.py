from flask import Flask
# from sampling import sample_uniform
from stochastic import get_words
from stochastic import count_words
from stochastic import random_word
from histogram import get_words
from higher_order_markov_chain import markov_chain
import random


app = Flask(__name__)

@app.route('/')
def hello_world():
    words_list = get_words('corpus.txt')
    chain = markov_chain(word_list)
    list_from_chain = list(chain)
    random_words = random.choice(list_from_chain)
    sentence = make_sentence(chain, random_words, 10)
    return str(sentence)
    # histograms = count_words(words_list)
    # words = []
    # for _ in range(0, 8):
    #     words.append(random_word(histograms))
    #     output = ' '.join(words)
    #     outputString = output
    # return str(outputString)

# print(hello_world())
#
# @app.route('/')
# def hello_world():
#     colors = ' red orange yellow green blue indigo violet'.split()
#     random_color = sample_uniform(colors)
#
#     return HTML.format(random_color)

#
# @app.route('/colors/<int:num>')
# def hello_world():
#     colors = ' red orange yellow green blue indigo violet'.split()
#     random_colors = []
#     for _ in range(num):
#         random_colors.append(sample_uniform(colors))
#     random_colors_str = ' '.join(random_colors)
#     return HTML.format(random_colors_str)
