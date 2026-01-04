from stats import get_num_words, get_char_nums, sort_char_nums
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    book = get_book_text(file_path)
    print("----------- Word Count ----------")
    words, num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print("----------- Word Count ----------")
    chars = get_char_nums(words)
    sort_char_nums(chars)
    print("============= END ===============")


if __name__ == "__main__":
    main()
