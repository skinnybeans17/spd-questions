digit_combos = {
    "9": ["z", "y", "x", "w"],
    "8": ["v", "u", "t"],
    "7": ["s", "r", "q", "p"],
    "6": ["o", "n", "m"],
    "5": ["l", "k", "j"],
    "4": ["i", "h", "g"],
    "3": ["f", "e", "d"],
    "2": ["c", "b", "a"],
}

def combo_letters(keys, loading=""):
    pressed_key = keys[0]
    values = []

    for letter in digit_combos[pressed_key]:

        if(len(keys) == 1):
            values.append(leading + letter)
        
        else:
            values += combo_letters(keys[1:], leading + letter)

    return values
    combo_letters(kets, "532")
    print(values)
