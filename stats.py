
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
