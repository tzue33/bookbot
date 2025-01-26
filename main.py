def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    list_num_chars = [{"character": char, "count": count} 
                      for char, count in num_chars.items()
                      if char.isalpha()]
    list_num_chars.sort(key=lambda char_dict: char_dict["count"], reverse=True)
    for item in list_num_chars:
        print(f"The '{item['character']}' character was found {item['count']} times")
    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    num_chars = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character not in num_chars:
            num_chars[character] = 1
        else: 
            num_chars[character] += 1
    return num_chars





main()
