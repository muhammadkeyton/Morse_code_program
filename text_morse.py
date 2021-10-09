
#splits characters in a string into individual characters in a list.
def split(word):
    return [char for char in word]

#splits morse characters by space in between them
def space(word):
    return word.split()


class Morse:
    def __init__(self, morse_ref, text):
        self.text = text
        self.morse_code = morse_ref
#converts text to morse code
    def to_morse(self):
        morse_message = ""
        characters = split(self.text)
        for char in characters:
            for letter, morse in self.morse_code.items():
                if letter == char:
                    morse_message += f"{morse} "
        return f"The morse-code is: {morse_message}"
#converts morse code to text
    def to_text(self):
        text_message = ""
        morse_characters = space(self.text)
        for morse_char in morse_characters:
            for letter, morse in self.morse_code.items():
                if morse == morse_char:
                    text_message += f"{letter} "
        return f"The morse-message is: {text_message}"
