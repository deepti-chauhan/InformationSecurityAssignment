# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher
# pip install egcd
# pip install numpy
"""
Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)
C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used
"""

import numpy as np
from egcd import egcd

alph = "abcdefghijklmnopqrstuvwxyz"

ltr_to_ind = dict(zip(alph, range(len(alph))))
ind_to_ltr = dict(zip(range(len(alph)), alph))


def mtrx_mod_inv(mtrx, modulus):
    """We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
    """

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    mtrx_modulus_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv


def encr(msg, K):
    encry = ""
    msg_in_num = []

    for ltr in msg:
        msg_in_num.append(ltr_to_ind[ltr])

    split_P = [
        msg_in_num[i: i + int(K.shape[0])]
        for i in range(0, len(msg_in_num), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, ltr_to_ind[" "])[:, np.newaxis]

        num = np.dot(K, P) % len(alphabet)
        n = num.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            num = int(num[idx, 0])
            encry += ind_to_ltr[num]

    return encry


def decry(cipher, Kinv):
    decry = ""
    cipher_in_num = []

    for ktr in cipher:
        cipher_in_num.append(ltr_to_ind[ltr])

    split_C = [
        cipher_in_num[i: i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_num), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        num = np.dot(Kinv, C) % len(alphabet)
        n = num.shape[0]

        for idx in range(n):
            numb = int(num[idx, 0])
            decry+= ind_to_ltr[num]

    return decry


def main():
    msg = 'ihateyou'

    K = np.mtrx([[3, 3], [2, 5]])

    Kinv = mtrx_mod_inv(K, len(alphabet))

    encry_msg = encry(msg, K)
    decry_msg = decry(encry_msg, Kinv)

    print("The Original message: " + msg)
    print("The Encrypted message: " + encry_msg)
    print("The Decrypted message: " + decry_msg)


main()


