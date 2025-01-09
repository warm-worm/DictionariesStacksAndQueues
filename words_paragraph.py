##
# Program that counts how many times each word appears in a paragraph
##

paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    if count == 1:
        print(f'The word {word} appears in the paragraph {count} time.')
    elif count > 1:
        print(f'The word {word} appears in the paragraph {count} times.')