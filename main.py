def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    sorted_characters = get_sorted_character_counts(character_counts)
    print_report(word_count, sorted_characters, book)

def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    counts = {}
    for letter in text:
        letter = letter.lower()
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

def sort_on(dict):
    return dict["count"]

def get_sorted_character_counts(character_counts):
    characters = [{"character": key, "count":character_counts[key]} for key in character_counts if key.isalpha()]
    characters.sort(reverse=True,key = sort_on)
    return characters

def print_report(word_count, sorted_characters, book):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n\n")
    for character in sorted_characters:
        print(f"The '{character['character']}' character was found '{character['count']}' times")

main()