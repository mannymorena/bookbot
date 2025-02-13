def main():
    book_path = "books/frankenstein.txt"
    text = read_from_book(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document.\n\n")
    report_data = count_chars(text)
    for key, value in report_data.items():
        print(f"The '{key}' character was found {value} times")

def count_words(text):
    words = text.split()
    return len(words)

def read_from_book(path):
    with open(path) as f:
        return f.read()
    
def count_chars(text):
    strings = set(text.lower())
    string_count = {}
    for string in strings:
          count = 0
          for letter in text.lower():
             if letter == string and letter not in [" ", ".", "#","\n"]:
                count += 1
                string_count[f"{string}"] = count
    return string_count

main()

