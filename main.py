def main():
    frnknstn_path = "books/frankenstein.txt"

    book = open_book(frnknstn_path)
    word_count = count_words(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    char_count = count_char(book)
    char_list = value_list(char_count)

    for dict in char_list:
        if dict['char'].isalpha():
            print(f"The '{dict['char']}' character was found {dict['value']} times")

    print("--- End report ---")

def open_book(path):

    with open(path) as f:
        return f.read()

def count_words(book):

    return len(book.split())

def count_char(book):
    char_dict = {}
    for char in book:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1

    return char_dict

def sort_on(dict):
    return dict["value"]

def value_list(dict):
    value_list = []
    for i in dict:
        value_list.append({"char": i, "value": dict[i]})
    value_list.sort(reverse=True, key=sort_on)

    return value_list



main()