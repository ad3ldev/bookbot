
def get_num_words(book_text):
    words = book_text.split()
    return words, len(words)


def get_char_nums(words):
    chars = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char not in chars:
                chars[char] = 1
                continue
            chars[char] += 1
    return chars


def sort_on(items):
    return items["count"]


def sort_char_nums(chars):
    count_array = []
    for c in chars:
        count_array.append({"char": c, "count": chars[c]})
    count_array.sort(reverse=True, key=sort_on)
    for i in count_array:
        print(f"{i["char"]}: {i["count"]}")
