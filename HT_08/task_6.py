""" 6. Напишіть функцію,яка прймає рядок з декількох слів і повертає
довжину найкоротшого слова. Реалізуйте обчислення за допомогою генератора.
"""


#def shortest_word_length(input_string):
#    return min([len(word) for word in input_string.split()])


def shortest_word_length(input_string):
    words_list = input_string.split()

    def get_next_word(words_list):
        for word in words_list:
            yield word

    words = get_next_word(words_list)
    
    shortest = len(next(words))

    while True:
        try:
            shortest = min(len(next(words)), shortest)
        except StopIteration:
            return shortest


print(shortest_word_length('shortest word length'))
