t9_map = {
    "9": ["z", "y", "x", "w"],
    "8": ["v", "u", "t"],
    "7": ["s", "r", "q", "p"],
    "6": ["o", "n", "m"],
    "5": ["l", "k", "j"],
    "4": ["i", "h", "g"],
    "3": ["f", "e", "d"],
    "2": ["c", "b", "a"],
}

def t9_letters(keys, loading=""):
    pressed_key = keys[0]
    values = []

    for letter in t9_map[pressed_key]:

        if(len(keys) == 1):
            values.append(leading + letter)
        
        else:
            values += t9_letters(keys[1:], leading + letter)

    return values
