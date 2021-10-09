from text_morse import Morse

#this dictionary contains letters & numbers with their morse-codes
letters_morsecode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z":"--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

end = False


while not end:
    option = input("To convert text to morse'press m',To convert morse to text'press t': ").lower()
    if option == "t":
        morse = input("Please enter your morse: ")
        print("")
        morse = Morse(morse_ref=letters_morsecode, text=morse)
        print(morse.to_text())
        end=True

    elif option == "m":
        message = input("Please enter the text you want to convert to morse: ").upper()
        print("")
        morse = Morse(morse_ref=letters_morsecode, text=message)
        print(morse.to_morse())
        end = True
    else:
        print("please type only t or m")


