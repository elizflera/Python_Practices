def main(x):
    A = x & 0b111111
    B = (x >> 6) & 0b111111
    C = (x >> 12) & 0b1
    D = (x >> 13) & 0b1111
    E = (x >> 17) & 0b11
    F = (x >> 19) & 0b11111111
    G = (x >> 27) & 0b1
    H = (x >> 28) & 0b11111
    res = 0
    res |= D
    res |= B << 4
    res |= H << 10
    res |= C << 14
    res |= G << 15
    res |= A << 16
    res |= E << 22
    res |= F << 24
    return res
