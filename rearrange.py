import sys
import random




param_1 = sys.argv[1]
param_2 = sys.argv[2]
param_3 = sys.argv[3]
param_4 = sys.argv[4]

quotes = [param_1,
          param_2,
          param_3,
          param_4]

newList = []

def random_python_quote():
    for i in range(0, len(quotes)):
        rand_index = random.randint(0, len(quotes) - 1)
        rand_singleQuote = quotes[rand_index]

        # pop from quotes using rand_index
        quotes.pop(rand_index)

        # create a new list for the new order

        newList.append(rand_singleQuote)

        # fill that list until we have all quotes in a new random order

        output = ' '.join(newList)
        hey = output
    return newList

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)


random_python_quote()
