def get_words(filename):
    all_words_list = []
    with open(filename) as file:
        for line in file:
            words_list = line.split()
            for word in words_list:
                all_words_list.append(word)
    return all_words_list




def list_count(word_list):
    big_list = []
    for word in word_list:
        for sub_list in big_list:
            if word == sub_list[0]:
                sub_list[1] += 1
                # stop iterating if you come across word
                break
        # If we dont come across word, add word
        else:
            list_to_append = [word, 1]
            big_list.append(list_to_append)
    return big_list


# word_list = get_words('LifeAndHabit.txt')
# counts = list_count(word_list)
# print(counts)
