def count_words(text: str):
    words = text.split()
    return len(words)

def count_characters(text: str):
    char_count = {}
    for character in text:
        if character.lower() in char_count:
            char_count[character.lower()] += 1
        else:
            char_count[character.lower()] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_characters(char_count: dict):
    dict_car_count = {"char": "", "num": 0}
    list_dict_char_count = []
    for char in char_count:
        dict_car_count["char"] = char
        dict_car_count["num"] = char_count[char]
        list_dict_char_count.append(dict_car_count.copy())
    list_dict_char_count.sort(reverse=True, key=sort_on)
    return list_dict_char_count