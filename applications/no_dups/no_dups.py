def no_dups(s):
    # Your code here
    word_cache = []
    words = s.split()
    for word in words:
        if word not in word_cache:
            word_cache.append(word)
    result = " ".join(word for word in word_cache)
    return result
        



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))