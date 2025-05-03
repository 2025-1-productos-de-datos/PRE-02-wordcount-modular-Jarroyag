 #obtain a list of files in the input directory
import sys

from internals.src._internals.count_words import count_words
from internals.src._internals.preprocess_lines import preprocess_lines
from internals.src._internals.split_into_words import split_into_words
from internals.src.read_all_lines import read_all_lines

from homework.src.write_word_counts import write_word_counts

from .internals.write_count_words import write_count_words


def main():

    
    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = "sys.argv[1]"
    output_folder = "sys.argv[2]"

    
    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
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
    write_word_counts(counter)

def read_all_lines():
    all_lines = read_all_lines()
    return all_lines

def new_func(all_lines):
    all_lines = [line.lower().strip() for line in all_lines]
    return all_lines


if __name__ == "__main__":
    main()
