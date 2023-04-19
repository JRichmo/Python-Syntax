
# For a list of words, print out each word on a separate line, all in uppercase
# Turn this into a function
def print_upper_words(words):
     for word in words:
      print (word.upper())

# change the function so that it only prints words that start with the letter 'e'
def print_words_with_e(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

# make the function more general: you should be able to pass in a set of letters and it only prints words that start with those letters

def print_gen_words(words,letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break



