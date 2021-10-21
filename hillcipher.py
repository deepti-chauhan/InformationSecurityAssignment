pip install egcd
pip install numpy

# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher
import numpy as np
from egcd import egcd

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def matrix_mod_inv(matrix, modulus):
    #determinant
    det = int(np.round(np.linalg.det(matrix)))

    #regularise determinant
    det_inv = egcd(det, modulus)[1] % modulus 
    matrix_modulus_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    ) 

    return matrix_modulus_inv


def encrypt(msg, K):
    encrypted = ""
    msg_in_numbers = []

    for letter in msg:
        msg_in_numbers.append(letter_to_index[letter])

    mapped_plainText = [
        msg_in_numbers[i: i + int(K.shape[0])]
        for i in range(0, len(msg_in_numbers), int(K.shape[0]))
    ]
    #encrypt text
    #P = D(K,C) = inv(K)*C (mod X)
    #P = vector of plain text
    for P in mapped_plainText:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        num = np.dot(K, P) % len(alphabet)
        n = num.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for i in range(n):
            number = int(num[i, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, K_inv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    mapped_cipherText = [
        cipher_in_numbers[i: i + int(K_inv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(K_inv.shape[0]))
    ]
    #C = E(K,P) = K*P (mod X)
    #C = vector of cipher text
    for C in mapped_cipherText:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        num = np.dot(K_inv, c) % 26

        for i in range(num.shape[0]):
            number = int(num[i, 0])
            decrypted += index_to_letter[number]

    return decrypted


def main():
    msg = 'hillcipher'

    K = np.matrix([[3, 3], [2, 5]])
    K_inv = matrix_mod_inv(K, len(alphabet))

    encrypted_msg = encrypt(msg, K)
    decrypted_msg = decrypt(encrypted_msg, K_inv)

    print("Original message: " + msg)
    print("Encrypted message: " + encrypted_msg)
    print("Decrypted message: " + decrypted_msg)

if __name__ == "__main__":
    main()
