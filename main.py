def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in report:
        print(f"The {item[0]} character was found {item[1]} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_report(chars_dict):
    char_list = list(chars_dict.items())
    report_list = []
    for char in char_list:
        if char[0].isalpha():
            report_list.append(char)
    report_list.sort(key=lambda a: a[1], reverse=True)
    return report_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
