def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        book_text = f.read()
    print(f"There are {count_words(book_text)} words in the book!")
    print(count_characters(book_text))

def count_words(book_text):
        words = book_text.split()
        return(len(words))

def count_characters(text):
    lowered_text = text.lower()
    Char_Dict = {}
    for letter in lowered_text:
        if letter in Char_Dict:
            Char_Dict[letter] += 1
        else:
            Char_Dict[letter] = 1
    return Char_Dict

def sort_on(Char_Dict):
    test_dict = {"a" : 1, "h" : 5, "i" : 20}
    test_dict.sort()
    print(test_dict)

if __name__ == "__main__":
    main()