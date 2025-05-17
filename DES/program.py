#Programa para el cálculo del algoritmo de cifrado

import fileinput

# Permutaciones usadas en S-DES
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def permute(bits, permutation):
    return ''.join([bits[i-1] for i in permutation])

def left_shift(bits, num_shifts):
    return bits[num_shifts:] + bits[:num_shifts]

def generate_subkeys(key):
    # P10 permutation
    permuted_key = permute(key, P10)
    left, right = permuted_key[:5], permuted_key[5:]

    # Left shifts
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    subkey1 = permute(left + right, P8)

    left = left_shift(left, 2)
    right = left_shift(right, 2)
    subkey2 = permute(left + right, P8)

    return subkey1, subkey2

def xor(bits1, bits2):
    return ''.join(['1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2)])

def sbox(input_bits, sbox):
    row = int(input_bits[0] + input_bits[3], 2)
    col = int(input_bits[1] + input_bits[2], 2)
    return format(sbox[row][col], '02b')

def fk(bits, subkey):
    left, right = bits[:4], bits[4:]
    
    # Expand and permute
    expanded_right = permute(right, EP)

    # XOR with subkey
    xored = xor(expanded_right, subkey)

    # S-box lookups
    left_sbox = sbox(xored[:4], S0)
    right_sbox = sbox(xored[4:], S1)

    # P4 permutation
    p4_result = permute(left_sbox + right_sbox, P4)

    # XOR with left half and concatenate with unchanged right half
    return xor(left, p4_result) + right

def sdes(bits, key, encrypt=True):
    subkey1, subkey2 = generate_subkeys(key)

    if not encrypt:
        subkey1, subkey2 = subkey2, subkey1

    # Initial permutation
    bits = permute(bits, IP)

    # First round
    bits = fk(bits, subkey1)
    
    # Switch left and right halves
    bits = bits[4:] + bits[:4]

    # Second round
    bits = fk(bits, subkey2)

    # Inverse initial permutation
    return permute(bits, IP_INV)

def process_input():
    lines = [line.strip() for line in fileinput.input()]
    operation = lines[0]
    key = lines[1]
    text = lines[2]

    if operation == 'E':
        result = sdes(text, key, encrypt=True)
    elif operation == 'D':
        result = sdes(text, key, encrypt=False)
    else:
        raise ValueError("Operación no válida")

    print(result)

if __name__ == "__main__":
    process_input()
