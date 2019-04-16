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

def count_animals(animals_list):
    """Count occurences in the given list of animals and
    return that data structure"""

    animals_counts = {}

    for animal_name in animals_list:
        # Check if we saw this animal before
        if animal_name in animals_counts:
            # increase its count by one
            animals_counts[animal_name] += 1
        else:
            #set its count to one
            animals_counts[animal_name] = 1

    return animals_counts
def print_table(animal_counts):
    """Prints out a table of animals and their counts."""
    print('Animal | Count')
    print('-------------')
    for animal_name in animal_counts:
        count = animal_counts[animal_name]
        print(f'{animal_name} | {count}')
    total_count = 0
    for count in animal_counts.values():
        total_count += count

    print('-------------')

    print('giraffe | 11')

# print_table('giraffe')
animals_list = get_words('animals.txt')
counts = count_animals(animals_list)
print(counts)
# print(get_words('animals.txt'))
# pprint(counts['giraffe'])
# pprint(print_table)
