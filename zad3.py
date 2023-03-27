def caesar_cipher(text, key, extra_alphabet=None):
    if extra_alphabet is None:
        extra_alphabet = []
    if extra_alphabet:
        alphabet = extra_alphabet
    else:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
    tmp = list(text)
    counter = 0
    extra_num = 0
    for i in text:
        i = i.lower()
        if alphabet.__contains__(i):
            index = alphabet.index(i)
            if index + key > len(alphabet) - 1:
                extra_num = index + key - (len(alphabet))
                while extra_num > len(alphabet) - 1:
                    extra_num = extra_num - (len(alphabet))
                i = alphabet[extra_num]
            else:
                i = alphabet[index + key]
        tmp[counter] = i
        counter += 1
    text = "".join(tmp)
    print(text)


caesar_cipher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 3, ["a", "B"])
