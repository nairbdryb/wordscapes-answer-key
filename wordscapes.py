import sys


if __name__ == '__main__':
    arguments = sys.argv[1:4]
    # arguments are letters, length, required letters
    if len(arguments) <= 0:
        print("Usage: python wordscapes.py <letters> [length] [required letters]\nWhere letters is a string of letters, \nlength is the length(integer) of the word, \nand required letters is a string of letters that must be in the word at the specified index. '*' and '.' are wildcards for required letters.")
        sys.exit(1)
    letters = arguments[0]
    if len(arguments) < 2:
        length = '*'
    else:
        length = arguments[1]
    if len(arguments) < 3:
        required = ''
    else:
        required = arguments[2]


    words = []
    with open('words_3_7.txt', 'r') as file:
        for line in file:
            # ensure length of word is correct
            if length != '*' and len(line.strip()) != int(length):
                continue

            # ensure correct letters are in word
            letters_not_reused = letters
            for char in line.strip():
                if char not in letters_not_reused:
                    break
                letters_not_reused = letters_not_reused.replace(char, '', 1)
            else:
                words.append(line.strip() + '\n')

    if required == '':
        print("".join(words))
        sys.exit(0)

    words_to_remove = []
    for word in words:
        for index, char in enumerate(word.strip()):
            if word[index] != required[index] and not ( required[index] == '*' or required[index] == '.' ):
                words_to_remove.append(word)
                break
    for word in words_to_remove:
        words.remove(word)
            
    print("".join(words))
            