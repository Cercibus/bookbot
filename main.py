import sys
from stats import get_char_incidence, get_book_length, char_by_incidence, numerical_value

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")

print("============ BOOKBOT ============")
print(f"Analyzing  book found at {sys.argv[1]}")
print("---------- Word Count ----------")
print(f"Found {get_book_length(sys.argv[1])} total words")
print("------- Character Count -------")
for entry in char_by_incidence(get_char_incidence(sys.argv[1])):
	if entry["char"].isalpha():
		print(f"{entry['char']}: {entry['num']}") 
print("=============== END ===============")
