from itertools import groupby


def bwt_direct(sequence):
    sequence += '#'
    table = [sequence[index:] + sequence[:index] for index, _ in enumerate(sequence)]
    table.sort()
    bwt = [rotation[-1] for rotation in table]
    bwt = ''.join(bwt)
    return bwt


def bwt_inv(sequence):
    table = [col for col in sequence]
    for i in range(len(sequence) - 1):
        table.sort()
        table = [sequence[i] + table[i] for i in range(len(sequence))]


    return table[[row[-1] for row in table].index('#')]


data = 'ABACABAABACABA'
print('Original data:', data)
res1 = bwt_direct(data)
data2 = res1.replace('#', '')
print('Result of direct BWT:', data2)

res2 = bwt_inv(res1)
print('Result of inverse BWT:', res2.replace('#', ''))


def rle_encode(data):
    return ''.join([str(k) + str(len(list(g))) for k, g in groupby(data)])


print('RLE on original:', rle_encode(data))
print('RLE on BWT:', rle_encode(data2))
