import sys
from stats import get_word_count, get_letter_counts, print_book_stats_report

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    word_count = get_word_count(book_contents)
    letter_count = get_letter_counts(book_contents)
    print_book_stats_report(word_count, letter_count, book_path)

main()