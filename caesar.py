# Copied functions from previous Caesar project

#from Caesar
def encrypt(text, rot):
    encrypted = ""
    for letter in text:
        encrypted += rotate_character(letter, rot)
    return encrypted

#from helpers

def alphabet_position(letter):
    letter = letter.upper()
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(letter)

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    pos = alphabet_position(char)
    rotpos = (pos + rot) % 26
    rotchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[rotpos]
    if char == char.upper():
        return rotchar
    else:
        return rotchar.lower()
