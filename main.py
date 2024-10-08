def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        book_text = f.read()
    word_count = count_words(book_text)
    char_list = sort_on(count_characters(book_text))
    print_report(word_count, char_list, path_to_file)

def count_words(book_text):
        words = book_text.split()
        return(len(words))

def count_characters(text):
    lowered_text = text.lower()
    Char_Dict = {}
    for letter in lowered_text:
        if letter.isalpha(): 
            if letter in Char_Dict:
                Char_Dict[letter] += 1
            else:
                Char_Dict[letter] = 1
    return Char_Dict

def sort_on(Char_Dict):
    char_list = list(Char_Dict.items())
    char_list.sort(key=lambda item: item[1], reverse=True)
    return char_list

def print_report(word_count, char_list, path_to_file):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document \n")
    for char, count in char_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()