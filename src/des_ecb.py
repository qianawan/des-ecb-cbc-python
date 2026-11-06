# coding:utf-8
IP = (58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7)
FP = (40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25)
E = (32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1)
P = (16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25)
S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
PC_1L = (57, 49, 41, 33, 25, 17, 9,
         1, 58, 50, 42, 34, 26, 18,
         10, 2, 59, 51, 43, 35, 27,
         19, 11, 3, 60, 52, 44, 36)
PC_1R = (63, 55, 47, 39, 31, 23, 15,
         7, 62, 54, 46, 38, 30, 22,
         14, 6, 61, 53, 45, 37, 29,
         21, 13, 5, 28, 20, 12, 4)
PC_2 = (14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32)


def Permute(block, b_len, PP):
    #The block is replaced by the permutation matrix PP, b_len is the block length (bit, bit) 
    res = 0
    for i in PP:
        res = res << 1
        # The i-1th position is the penultimate
        res |= (block >> (b_len - i)) & 0x01
    return res


def bytesToblocks(m):
    # Byte sequence conversion bit blocks    b'\x00\x01\x02\x03\xff\xff\xff\xff' -> [0x00010203,0xffffffff]
    while len(m) % 8 != 0:
        m += b'\x00'
    blocks = []
    for i in range(len(m) // 4):
        blocks.append((m[4 * i] << 24) | (m[4 * i + 1] << 16) |
                      (m[4 * i + 2] << 8) | (m[4 * i + 3]))
    return blocks


def blocksTobytes(blocks):
    #blocks are converted to byte sequences     [0x00010203,0xffffffff] -> b'\x00\x01\x02\x03\xff\xff\xff\xff'
    res = b''
    for i in blocks:
        res += i.to_bytes(4, byteorder="big")
    return res


L = lambda x, n: ((x << n) | (x >> (28 - n))) & 0x0fffffff
# Rotate a 28bits number x to the left by n bits

class DES(object):

    def F(self, block, subKeyid):
        """
        :param block: 32bits
        :param subKeyid:
        :return: res: 32bits
        """
        temp = Permute(block, 32, E) ^ self.subKs[subKeyid]
        res = 0
        for i in range(8):
            res = res << 4
            yxxxxy = (temp >> 6 * (7 - i)) & 0x3f
            xxxx = (yxxxxy & 0x1f) >> 1
            yy = ((yxxxxy >> 5) << 1) | (yxxxxy & 0x01)
            res |= S[i][yy][xxxx]
        res = Permute(res, 32, P)
        return res & 0xffffffff

    def __init__(self, K: bytes):
        #Generate an instance by key K 
        self.K = K
        self.K_blocks = bytesToblocks(K)[:2]
        #generate word key self.subKs[16]
        self.subKs = None
        self.generate_subKs()

    def Encrypt(self, m: bytes) -> bytes:
        # encryption
        blocks = bytesToblocks(m)
        cblocks = []
        for i in range(len(blocks) // 2):
            #Each 64bits high 32bits, low 32bits 
            high, low = blocks[2 * i], blocks[2 * i + 1]
            # Step 1: Initial Replacement IP
            temp = Permute((high << 32) | low, 64, IP) & 0xffffffffffffffff
            # Step 2: Get Li and Ri
            high, low = temp >> 32, temp & 0xffffffff
            # Step 3: A total of 16 iterations
            for j in range(16):
                high, low = low, (high ^ self.F(low, j))
            #Step 4: Merge L16 and R16, pay attention to merge into R16L16 
            high, low = low, high
            # Step 5: Replace FP at the end
            temp = Permute((high << 32) | low, 64, FP) & 0xffffffffffffffff
            high, low = temp >> 32, temp & 0xffffffff
            cblocks.append(high)
            cblocks.append(low)
        return blocksTobytes(cblocks)

    def Decrypt(self, e: bytes) -> bytes:
        #decrypt 
        blocks = bytesToblocks(e)
        cblocks = []
        for i in range(len(blocks) // 2):
            # Each 64bits high 32bits, low 32bits
            high, low = blocks[2 * i], blocks[2 * i + 1]
            # Step 1: Initial Replacement IP
            temp = Permute((high << 32) | low, 64, IP) & 0xffffffffffffffff
            #Step 2: Get Li and Ri
            high, low = temp >> 32, temp & 0xffffffff
            #Step 3: A total of 16 rounds of iterations, the subkeys are reversed 
            for j in range(16):
                high, low = low, (high ^ self.F(low, 15 - j))
            #Step 4: Merge L16 and R16, pay attention to merge into R16L16
            high, low = low, high
            #Step 5: Replace FP at the end
            temp = Permute((high << 32) | low, 64, FP) & 0xffffffffffffffff
            high, low = temp >> 32, temp & 0xffffffff
            cblocks.append(high)
            cblocks.append(low)
        return blocksTobytes(cblocks)

    def generate_subKs(self):
        # print(bin((self.K_blocks[0] << 32) | self.K_blocks[1])[2:].rjust(32, '0'))
        C = Permute((self.K_blocks[0] << 32) | self.K_blocks[1], 64, PC_1L)  & 0x0fffffff
        D = Permute((self.K_blocks[0] << 32) | self.K_blocks[1], 64, PC_1R)  & 0x0fffffff
        # print(bin(C)[2:].rjust(28, '0'))
        # print(bin(D)[2:].rjust(28, '0'))
        self.subKs = []
        for i in range(16):
            if i in (0, 1, 8, 15):
                C, D = L(C, 1), L(D, 1)
            else:
                C, D = L(C, 2), L(D, 2)
            self.subKs.append(Permute((C << 28) | D, 56, PC_2))
            # print(hex(self.subKs[i]))

    def getK(self) -> bytes:
        # return key K
        return self.K

    def generateK(self) -> bytes:
        #Randomly generate the key K
        pass


def print_bytes_hex(m):
    str=""
    for i in m:
        # print(hex(i)[2:].rjust(2, '0'), end='')
        str+=hex(i)[2:].rjust(2, '0')
    # print()
    return str
if __name__ == '__main__':
    #If the key is less than 64bits, add zeros, if it is more than 64bits, use the first 64bits 
    # messages Multiples of less than 64bits fill with zeros
    m = b'wanwei33' # plain text
    k = b'00101010' # key
    a = DES(k)
    cc = a.Encrypt(m)
    mm = a.Decrypt(cc)
    print("plain text:", end='')
    print(m.decode('UTF-8'))
    print("key:", end='')
    print(a.K.decode('UTF-8'))
    print("ciphertext:", end='')
    str = print_bytes_hex(cc)  # Output in bytes
    print(str)
    print("decrypt:", end='')
    print(mm)
