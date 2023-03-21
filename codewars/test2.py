caca = "11111101"

def decode_bits(bits):
    bits = bits.strip("0")
    n = min([len(x) for x in bits.split("1") + bits.split("0") if len(x) > 0])
    bits = bits.replace(f'{(3 * n) * "1"}', "-")
    bits = bits.replace(f'{(1 * n) * "1"}', ".")
    bits = bits.replace(f'{(7 * n) * "0"}', "   ")
    bits = bits.replace(f'{(3 * n) * "0"}', " ")
    bits = bits.replace("0", "")
    return bits

