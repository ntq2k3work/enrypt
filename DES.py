IP_1 = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_2 = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

S_BOX = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC_2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

T = [
    1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]


def message_input():
    while True:
        message = str(input("Nhập chuỗi mã hoá = "))
        if len(message) == 8:
            return message
        else:
            print("Nhập input có độ dài = 8")


def key_input():
    while True:
        key = str(input("Nhập key mã hoá = "))
        if len(key) == 8:
            return key
        else:
            print("Key phải có độ dài = 8")


def print_key(key):
    for i in range(16):
        print(f"key[{i}]: {key[i]}")
        


def menu():
    message = ""
    key = 0
    while True:
        print("1. Nhập chuỗi và khoá \n"
              "2. Mã hoá chuỗi\n"
              "3. Giải mã chuỗi")
        opt = int(input("Select option = "))
        match opt:
            case 1:
                message = message_input()
                key = key_input()
            case 2:
                result = encryption(message, key)
                message = result["text"]
                # print_key(result["key"])
                print("ciphertext: " + message)
            case 3:
                result = decryption(message, key)
                message = result["text"]
                # print_key(result["key"])
                print("plaintext: " + message)
            case _:
                return


def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]

# Chuyển chuỗi sang nhị phân
def text_binary(x):
    end = ""
    for char in x:
        # ord để lấy mã unicode của kí tự char
        bi = convert_binary(ord(char))
        # zfill để thêm 0 vào đầu chuỗi bi
        end += bi.zfill(8)
    return [int(i) for i in end.zfill(64)]

# Chuyển nhị phân sang chuỗi
def binary_text(x):
    end = ""
    for i in range(0, 64, 8):
        end += chr(convert_number(x[i:i + 8]))
    return end

# Chuyển thập phân sang nhị phân
def convert_binary(x):
    # [2:] để bỏ 2 kí tự Ob ở đầu
    return bin(int(hex(x), 16))[2:]

# Chuyển nhị phân -> thập phân
def convert_number(x):
    return int("0b" + x, 2)


def swap(a, box):
    return [a[i - 1] for i in box]

# Dịch trái
def shift_left(arr, n):
    return arr[n:] + [0] * n


def create_key(key):
    k = [[0]] * 16
    pc_1 = swap(key, PC_1)
    c = pc_1[:28]
    d = pc_1[28:]
    for i in range(16):
        c = shift_left(c, T[i])
        d = shift_left(d, T[i])
        k[i] = (swap(c + d, PC_2))
    return k


def encryption(message, key):
    message_bi = text_binary(message)
    k = create_key(text_binary(key))
    ip_1 = swap(message_bi, IP_1)
    left = ip_1[:32]
    right = ip_1[32:]
    for i in range(16):
        temp = [i for i in left]
        left = [i for i in right]
        x = xor(swap(right, E), k[i])
        s = []
        for j in range(0, 48, 6):
            block = "".join(str(i) for i in x[j:j + 6])
            row = convert_number(block[0] + block[-1])
            col = convert_number(block[1:-2])
            si = convert_binary(S_BOX[int(j / 6)][row][col]).zfill(4)
            s += [int(w) for w in si]
        right = xor(temp, swap(s, P))
    ip_2 = swap(right + left, IP_2)
    end = "".join([str(i) for i in ip_2])
    return {
        "key": k,
        "text": binary_text(end)
    }


def decryption(message, key):
    message_bi = text_binary(message)
    k = create_key(text_binary(key))
    ip_1 = swap(message_bi, IP_1)
    right = ip_1[:32]
    left = ip_1[32:]
    for i in range(16):
        temp = [i for i in right]
        right = [i for i in left]
        x = xor(swap(left, E), k[15 - i])
        s = []
        for j in range(0, 48, 6):
            block = "".join(str(i) for i in x[j:j + 6])
            row = convert_number(block[0] + block[-1])
            col = convert_number(block[1:-2])
            si = convert_binary(S_BOX[int(j / 6)][row][col]).zfill(4)
            s += [int(w) for w in si]
        left = xor(temp, swap(s, P))
    ip_2 = swap(left + right, IP_2)
    end = "".join([str(i) for i in ip_2])
    return {
        "key": k,
        "text": binary_text(end)
    }


menu()
