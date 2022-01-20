def print_upper_words1(words):
    """Print each word on separate line; uppercased

    For example:
        print_upper_words1(["elephant", "Elf", "Dumbo"])
        ELEPHANT
        ELF
        DUMBO
    """
    for word in words:
        print(word.upper())

# print_upper_words1(["elephant", "Elf", "Dumbo"])


def print_upper_words2(words):
    """Print each word on separate line; uppercased; if starts with the letter ‘e’ (either upper or lowercase).

    For example:
        print_upper_words2(["elephant", "Elf", "Dumbo"])
        ELEPHANT
        ELF
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

# print_upper_words2(["elephant", "Elf", "Dumbo"])


def print_upper_words3(words, must_start_with):
    """Print each word on separate line; uppercased; pass in a set of letters, and it only prints words that start with one of those letters

    For example:
        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
        "HELLO"
        "HEY"
        "YO"
        "YES"
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
