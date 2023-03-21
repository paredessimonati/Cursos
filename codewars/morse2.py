def decode_bits(bits):
    bits = bits.strip("0")
    n = min([len(x) for x in bits.split("1") + bits.split("0") if len(x) > 0])
    bits = bits.replace((3 * n) * "1", "-")
    bits = bits.replace((1 * n) * "1", ".")
    bits = bits.replace((7 * n) * "0", "   ")
    bits = bits.replace((3 * n) * "0", " ")
    bits = bits.replace("0", "")
    return bits

def decode_morse(morse_code):
    symbols = morse_code.strip().replace("   ", " x ").split()
    return "".join(MORSE_CODE.get(symbol, " ") for symbol in symbols)