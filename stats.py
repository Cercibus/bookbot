def get_book_length(path):
        with open(path) as f:
                words = len(f.read().split())
                return words

def get_char_incidence(path):
	count = {}
	with open(path) as f:
		characters = list(f.read().lower())
		for character in characters:
			if character not in count:
				count[character] = 1
			else:
				count[character] += 1
	return count

def numerical_value(dict):
	return dict["num"]

def char_by_incidence(count):
	organized = []
	for character in count:
		char = {"char": character, "num": count[character]}
		organized.append(char)
	organized.sort(reverse=True, key=numerical_value)
	return organized
