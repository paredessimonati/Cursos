from preloaded import MORSE_CODE

def decode_morse(morse_code):
    text = morse_code.strip().replace("   ", " x ").split()
    text = [" " if item == "x" else MORSE_CODE[item] for item in text]
    return "".join(text)