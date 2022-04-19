import struct


def main(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        le = 10
        a1 = [struct_b(offset + i * le) for i in range(4)]
        offset += le * 4
        [a2] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        a3 = struct_d(offset)
        offset += 52
        [a4] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        return {
            'A1': a1,
            'A2': struct_c(a2),
            'A3': a3,
            'A4': a4,
        }

    def struct_b(offset: int) -> dict:
        [b1] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [b2] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4
        [b3] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        return {
            'B1': b1,
            'B2': b2,
            'B3': b3,
        }

    def struct_c(offset: int) -> dict:
        [c1] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [c2] = struct.unpack('> Q', binary[offset: offset + 8])
        offset += 8
        [length1] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [link_str] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        c3 = list(struct.unpack('> ' + str(length1) + 'c',
                                binary[link_str: link_str + length1]))
        c3 = [i.decode('UTF-8') for i in c3]
        [c4] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2

        return {
            'C1': c1,
            'C2': c2,
            'C3': "".join(c3),
            'C4': c4,
        }

    def struct_d(offset: int) -> dict:
        d1 = struct_e(offset)
        offset += 6
        [d2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [d3] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1
        [length1] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [link_str] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        d4 = list(struct.unpack('> ' + str(length1) + 'b',
                                binary[link_str: link_str + length1]))
        [d5] = struct.unpack('> Q', binary[offset: offset + 8])
        offset += 8
        [length1] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [link_str] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        d6 = list(struct.unpack('> ' + str(length1) + 'Q',
                                binary[link_str: link_str + length1 * 8]))
        d7 = list(struct.unpack('> 2i',
                                binary[offset: offset + 8]))
        offset += 8
        d8 = struct_f(offset)
        offset += 13

        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
            'D5': d5,
            'D6': d6,
            'D7': d7,
            'D8': d8,
        }

    def struct_e(offset: int) -> dict:
        [e1] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        [e2] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4

        return {
            'E1': e1,
            'E2': e2,
        }

    def struct_f(offset: int) -> dict:
        [f1] = struct.unpack('> d', binary[offset: offset + 8])
        offset += 8
        [f2] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4
        [f3] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1

        return {
            'F1': f1,
            'F2': f2,
            'F3': f3,
        }

    return struct_a(4)

print(main(b'\xa4IJT.\xeb\xfe\xf4\xc7\xd1\x05\x17b^k\xd9\xdd(\x13\xb8Ge\x87\x9d\x8beD\x8f'
 b'\xe9\xdcw\x99\x941\x9e\x16/\x92`\x17\xfc\xc8\xc6\x02\x00\x00\x00k\x93h*\n'
 b"\xa2\xb2\x94I\x95\x00\x00\x00\x03\x00\x00\x00}\xf9XH'\x81#e)\x00\x00\x00"
 b'\x02\x00\x80\x0cRu4\xc9\xb1;\xc9\xbf\xd3o\x15\r*2\xf8-*\xd5\xf4\xcd4\x1apx'
 b'mpg\xf5\x0b\xb5\xa7\x88$\xcc\xb6\xd4k\x00\x05\x00\x00\x00fBc\xfa\x96\xbenB"B'
 b'o\xd8\xf7()e\xc7K,\x12u\x8b'))
