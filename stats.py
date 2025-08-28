
def get_num_words(txt):
    words = txt.split()
    return len(words)

def get_chars_dict(txt):
    chars = {}
    for c in txt:
        low = c.lower()
        if low in chars:
            chars[low] += 1
        else:
            chars[low] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "count": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["count"]
