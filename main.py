from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath: str):
    file_contents = 0
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    # path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    char_count = sort_characters(char_count)
    # print(f"Found {num_words} total words.")
    # print(char_count)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("-------- Character Count -------")
    for char_info in char_count:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
