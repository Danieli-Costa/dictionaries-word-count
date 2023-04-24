"""Count words in file."""
import sys

# put your code here.
# read_file = open(sys.argv[1])


# word_counts = {}

# for line in read_file:
#     line = line.rstrip()
#     words = line.split()

#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1

# for word, count in word_counts.items():
#     print(word, count)  


# read_file = open(sys.argv[1])

# word_counts = {}

# for line in read_file:
#     line = line.rstrip()
#     words = line.split()

#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1

# for word, count in word_counts.items():
#     print(word, count)  



#  refactor code into functions



def tokenize(filename):
    words = []

    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            word = line.split()
            words.extend(word) #use extend not append

    return words

def count_words(words):
    word_count={}

    for word in words:
        word_count[word] = word_count.get(word, 0)+1

    return word_count

    
def print_word_counts(word_count):
     for word, count in word_count.items():
        print(word, count)  



filename = sys.argv[1]
words = tokenize(filename)
word_count = count_words(words)

print_word_counts(word_count)