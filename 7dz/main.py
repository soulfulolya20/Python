def main(x):
    A = x & 0b1
    B = (x >> 1) & 0b111111111
    C = (x >> 10) & 0b111111111111
    D = (x >> 22) & 0b1111111
    E = (x >> 29) & 0b11
    F = (x >> 31) & 0b1
    result = 0
    result |= A
    result |= C << 1
    result |= D << 13
    result |= B << 20
    result |= E << 29
    result |= F << 31
    return result

print(main(0xdaf51ff4))
