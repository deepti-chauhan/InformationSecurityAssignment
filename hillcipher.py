'''Hill cipher is a polygraphic substitution cipher based on linear algebra.
   Each letter is represented by a number modulo 26.'''

key_matrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
message_vector = [[0] for i in range(3)]

# Generate vector for the cipher
cipher+matrix = [[0] for i in range(3)]

# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			key_matrix[i][j] = ord(key[k]) % 65
			k += 1

# Following function encrypts the message
def encrypt(message_vector):
	for i in range(3):
		for j in range(1):
			cipher_matrix[i][j] = 0
			for x in range(3):
				cipher_matrix[i][j] += (key_matrix[i][x] *
									message_vector[x][j])
			cipher_matrix[i][j] = cipher_matrix[i][j] % 26

def HillCipher(message, key):

	# Get key matrix from the key string
	getKeyMatrix(key)

	# Generate vector for the message
	for i in range(3):
		message_vector[i][0] = ord(message[i]) % 65

	# Following function generates
	# the encrypted vector
	encrypt(message_vector)

	# Generate the encrypted text
	# from the encrypted vector
	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipher_matrix[i][0] + 65))

	# Finally print the ciphertext
	print("Ciphertext: ", "".join(CipherText))

def main():

	# Get the message to
	# be encrypted
	message = "HILLCIPHER"

	# Get the key
	key = "GYBNQKURP"

	HillCipher(message, key)

if __name__ == "__main__":
	main()
