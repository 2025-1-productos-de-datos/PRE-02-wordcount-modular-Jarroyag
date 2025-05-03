 #obtain a list of files in the input directory

from internals.src._internals.preprocess_lines import preprocess_lines
from internals.src._internals.split_in_words import split_in_words
from internals.src.read_all_lines import read_all_lines

from .internals.write_count_words import write_count_words


def main():

    
    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_in_words(all_lines)
    counter = count_words(words,output_folder)
    write_count_words(counter, output_folder)

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_count_words(counter)

def read_all_lines():
    all_lines = read_all_lines()
    return all_lines

def count_words(words):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

def new_func(all_lines):
    all_lines = [line.lower().strip() for line in all_lines]
    return all_lines


if __name__ == "__main__":
    main()
