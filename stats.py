def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count        

def sort_characters(char_count):
    # Build a list of {'char': <char>, 'num': <count>} dicts
    items = [{'char': key, 'num': value} for key, value in char_count.items()]
    # Sort the list by the numeric count descending and return it
    items.sort(key=lambda d: d['num'], reverse=True)
    final_dict = {d['char']: d['num'] for d in items}
    return final_dict
    
