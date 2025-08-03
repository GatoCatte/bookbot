def get_num_words(book_content):
    word_list = book_content.split()
    num_words = len(word_list)
    return num_words

def get_num_characters(book_content):
    characters = book_content.lower()
    num_characters = {}
    for character in characters:
        if character not in num_characters:
            num_characters[character] = 1
        else:
            num_characters[character] += 1
    return num_characters

def sort_characters(num_characters):
    sort = []
    for char, count in num_characters.items():
        if char.isalpha():
            sort.append({"char": char, "num": count})
    def sort_on(items):
        return items["num"]
    sort.sort(reverse=True, key=sort_on)
    return sort