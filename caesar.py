import string


def encrypt(text, rot):
    word = ""
    for char in text:
        word = word + rotate_character(char, rot)
    return word

def alphabet_position(letter):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    if letter in lowercase or letter in uppercase:
        indexNum = lowercase.index(letter.lower())
        return indexNum
    else:
        return letter

def rotate_character(char, rot):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    if char in lowercase:
        newInt = (alphabet_position(char) + rot) % 26
        return lowercase[newInt]
    elif char in uppercase:
        newInt = (alphabet_position(char) + rot) % 26
        return uppercase[newInt]
    else:
        return char
