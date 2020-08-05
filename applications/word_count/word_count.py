import re

def word_count(s):
    # Your code here
    word_dict = {}
    words = s.split()
    # add each word as a key
    ignore = '[.":;,-+=/\|[]{}()*^&]'
    for word in words:
        # before this was .isalnum which was clear of special characters but also got rid of the ' in doesn't
        filtered = ''.join(letter for letter in word if not letter == re.match(letter,ignore))
        key_word = filtered.lower()
        print("KEY WORD", key_word)
        # if the key exist, iterate the value of that key
        if key_word not in word_dict:
            word_dict[key_word] = 1
        else:
            word_dict[key_word] += 1
    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))