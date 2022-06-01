from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d',
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'int32')
    a2, offs = parse_b(buf, offs)
    a3, offs = parse(buf, offs, 'uint32')
    a4, offs = parse_e(buf, offs)
    a5, offs = parse_f(buf, offs)
    a6, offs = parse(buf, offs, 'int64')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint32')
    b2, offs = parse(buf, offs, 'float')
    b3, offs = parse_c(buf, offs)
    b4, offs = parse(buf, offs, 'int8')
    b5_size, offs = parse(buf, offs, 'uint32')
    b5_offs, offs = parse(buf, offs, 'uint16')
    b5 = []
    for _ in range(b5_size):
        val, b5_offs = parse_d(buf, b5_offs)
        b5.append(val)
    b6, offs = parse(buf, offs, 'uint64')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int32')
    c2, offs = parse(buf, offs, 'int8')
    c3, offs = parse(buf, offs, 'int8')
    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'double')
    d2_size, offs = parse(buf, offs, 'uint16')
    d2_offs, offs = parse(buf, offs, 'uint16')
    d2 = []
    for _ in range(d2_size):
        val, d2_offs = parse(buf, d2_offs, 'uint16')
        d2.append(val)
    return dict(D1=d1, D2=d2), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'uint16')
    e2, offs = parse(buf, offs, 'uint16')
    return dict(E1=e1, E2=e2), offs


def parse_f(buf, offs):
    f1_offs, offs = parse(buf, offs, 'uint16')
    f1, TT = parse_g(buf, f1_offs)
    f2 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'uint32')
        f2.append(val)
    f3, offs = parse(buf, offs, 'uint8')
    return dict(F1=f1, F2=f2, F3=f3), offs


def parse_g(buf, offs):
    g1, offs = parse(buf, offs, 'double')
    g2 = []
    for _ in range(8):
        val, offs = parse(buf, offs, 'uint8')
        g2.append(val)
    g3, offs = parse(buf, offs, 'int8')
    g4, offs = parse(buf, offs, 'int64')
    return dict(G1=g1, G2=g2, G3=g3, G4=g4), offs


def main(buf):
    return parse_a(buf, 4)[0]


buf2 = b'AVPHa\xecZ\xaf</\x1e9\xd4=}?\xbd\t\xa1\x83\xc8\xfb\x17\x02\x00\x00\x00f' \
       b'\x00$\xf3\x87XJ/\x80\xf75b\xa2G~/,\xb5~\x00mHG\xe735$\x05g\x0c\x9fd\xcd' \
       b'\xea\x1f\xeb)\n\xae\xc2;,J\xb4b\x8a\x8ft\xca\x05\x11\x19\xe1\xacO\xee+' \
       b"f\x04\x9c\xd3\xc0\xa3\xf5\xd7lp:r\x9b'\x86\x98\xe7XP6\x13B\xe82\xb2?\x04\x00" \
       b'T\x00\x00\x13\x00S\x15\xf0\xbf\xbf\x05\x00\\\x00\xfa\xbav\xbcW\xa1' \
       b'\xe6\xbf\xa3\xd0\xfd\x84x\xa3wN\t\xdaX\xca\x88\xa35\xabv'

buf1 = b"AVPH\x1a\x8d\xbb'b\x19f\xcf\x02\xe2C\xbf,\xc0Jk\xc2\xbc\t\x02\x00\x00\x00d" \
       b'\x00\xfa\xd2\xf5Eedhm;\x8f\x0e \xb8\xccg\xe2|\x00\x02\x8f\xd9D\xb5' \
       b'\x9c+\x9e\x98\xd6\xbaz\xe7\x92\xf2\x17\x8c\xd87^z+*\xd4c4\x9d1\xb4ke\xac\xb7' \
       b'\xf7\xcaP3\x9b\\>39\x06%\x94\xf9\xb3\xb3\x15|\xf1 V\xecf\xdc\xba' \
       b'\xff\x8a\xec\xbf\x04\x00T\x00\x10E\xa0\x91\x05\x93\xce?\x04\x00\\\x00' \
       b'*\x8a\xa8<b{\xe6\xbf\xe6\xbb\xe1\x83l!\x93v\x0fe\xb9o\xf7\xa9\x0eX\xe3'

print(main(buf2))

print()

print(main(buf1))
