#!/usr/bin/env python3

# Python 3.9.5

# morse_code_decipherment.py

# Signal interpretation:
# * short
# - long

ALPHABET_TO_MORSE = {'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**', 'E': '*', 'F': '**-*', 
            'G': '--*', 'H': '****', 'I': '**', 'J': '*----', 'K': '-*-', 'L': '*-**', 'M': '--',
            'N': '-*', 'O': '---', 'P': '*--*', 'Q': '--*-', 'R': '*-*', 'S': '***', 'T': '-',
            'U': '**-', 'V': '***-', 'W': '*--', 'X': '-**-', 'Y': '-*--', 'Z': '--**', '1': '*----',
            '2': '**---', '3': '***--', '4': '****-', '5': '*****', '6': '-****', '7': '--***', '8': '---**',
            '9': '----*', '0': '-----', '.': '*-*-*-', ',': '--**--', ':': '---***', ';': '-*-*-*', '?': '**--**',
            '!': '-*-*--', '-': '-****-'}

MORSE_TO_ALPHABET = {'*-': 'A', '-***': 'B', '-*-*': 'C', '-**': 'D', '*': 'E', '**-*': 'F', 
            '--*': 'G', '****': 'H', '**': 'I', '*----': 'J', '-*-': 'K', '*-**': 'L', '--': 'M',
            '-*': 'N', '---': 'O', '*--*': 'P', '--*-': 'Q', '*-*': 'R', '***': 'S', '-': 'T',
            '**-': 'U', '***-': 'V', '*--': 'W', '-**-': 'X', '-*--': 'Y', '--**': 'Z', '*----': '1',
            '**---': '2', '***--': '3', '****-': '4', '*****': '5', '-****': '6', '--***': '7', '---**': '8',
            '----*': '9', '-----': '0', '*-*-*-': '.', '--**--': ',', '---***': ':', '-*-*-*': ';', '**--**': '?',
            '-*-*--': '!', '-****-': '-'}

def alphabet_to_morse_code(sentence):
    morse_code = ""
    words = sentence.split()
    for word in words:
        for letter in word:
            for key in ALPHABET_TO_MORSE:
                if letter.capitalize() == key:
                    morse_code += ALPHABET_TO_MORSE[key]
            morse_code += " "
    return morse_code[0:-1]

def morse_to_alphabet(morse_to_sentence):
    translated = ""
    words = morse_to_sentence.split()
    for word in words:
        for key in MORSE_TO_ALPHABET:
            if key == word:
                translated += MORSE_TO_ALPHABET[key]
        translated += " "
    return translated[0:-1]

if __name__ == '__main__':
    phrase = 'help me, sos!'
    sentence_to_morse = alphabet_to_morse_code(phrase)
    print(sentence_to_morse)
    morse_to_sentence = morse_to_alphabet(sentence_to_morse)
    print(morse_to_sentence)
