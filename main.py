book_path = "books/frankenstein.txt"


def read_from_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
def count_chars(text):
    strings = set(text.lower())
    string_count = {}
    for string in strings:
          count = 0
          for letter in text.lower():
             if letter == string and letter not in [" ", ".", "#","\n"]:
                count += 1
                string_count[f"{string}"] = count
    for key, value in string_count.items():
        print(f"The '{key}' character was found {value} times")
    #return string_count

def main():
    text = read_from_book(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document.\n")
    count_chars(text)


main()

