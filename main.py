def get_book_data(file_path):
    """Returns the data of a text file, given a path."""

    # Import the data from the file
    with open(file_path) as f:
        file_contents = f.read()
        print(f"Imported book context as: {type(file_contents)}")

    return file_contents

def count_words(book_text):
    """Returns the number of words, given a book's text."""
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_characters(book_text):
    """Counts the number of characters of a given book's text"""
    character_counts = {}

    for character in book_text:
        char_lower = character.lower()
        if char_lower in character_counts:
            character_counts[char_lower] = character_counts[char_lower] + 1
        else:
            character_counts[char_lower] = 1
    
    return dict(sorted(character_counts.items()))


def main():
    '''Read the text of frankenstein'''
    # Set the path to the book
    path_to_book = "books/frankenstein.txt"

    # Import the data from the file
    frankenstein_text = get_book_data(path_to_book)

    # Print the file
    print(frankenstein_text)
    print("=========")

    # Print the wordcount
    word_count = count_words(frankenstein_text)
    print(word_count)

    # Print the character count dict object
    character_counts = count_characters(frankenstein_text)
    print(character_counts)

main()