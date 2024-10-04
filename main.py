
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        book_text = f.read()
    word_count = count_words(book_text)
    print(word_count)
def count_words(book_text):
        words = book_text.split()
        return(len(words))

if __name__ == "__main__":
    main()