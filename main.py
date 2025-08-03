from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    num_characters = get_num_characters(book_content)
    sort = sort_characters(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    #print(num_characters)
    #print(sort)
main()