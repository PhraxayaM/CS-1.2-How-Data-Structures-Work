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
        for baby_tuple in big_list:
            if word == baby_tuple[0]:
                count = baby_tuple[1]
                new_tuple = (word, count+1)
                #remove the old tuple
                big_list.remove(baby_tuple)

                #add the new tuple to big list
                big_list.append(new_tuple)

                # stop iterating if you come across word
                break
        # If we dont come across word, add word
        else:
            tuple_to_append = (word, 1)
            big_list.append(tuple_to_append)
    return big_list


word_list = get_words('fish.txt')
counts = list_count(word_list)
print(counts)
