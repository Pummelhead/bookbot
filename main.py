def main():
    book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #print(text)
    print(f"{get_word_count(book_path)} words found in the document")
    #print(get_letter_count(book_path))
    sort_letters(get_letter_count(book_path))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    count = 0
    words = get_book_text(path).split()
    for word in words:
        count += 1
    return count

def get_letter_count(path):
    letter_dict = {}
    words = get_book_text(path).lower()
    for word in words:
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

def sort_letters(letter_dict):
    lst_letters = list(letter_dict.items())
    lst_letters.sort(key = lambda a: -a[1])
    for letter in lst_letters:
        if letter[0].isalpha():
            print(f"The {letter[0]} character was found {letter[1]} times")
        
main()