from stats import word_count
from stats import count_characters
from stats import sort_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as f:
        return str(f.read())
    

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    final = sort_characters(count_characters(get_book_text(sys.argv[1])))
    for char,count in final.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    
main()  

